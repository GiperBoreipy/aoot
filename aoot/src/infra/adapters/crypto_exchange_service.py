from decimal import Decimal
from typing import override, Final, Any
from datetime import datetime, timezone
import base64
import hashlib
import hmac
import json

from aiohttp import ClientSession

from src.application.ports import CryptoExchangeService

from src.domain.tokens import Token, Ticker

from src.bootstrap.configs import Account


class OkxCryptoExchangeServiceImpl(CryptoExchangeService):
    BASE_API_URL: Final[str] = "https://www.okx.com"

    def __init__(self, http_client: ClientSession) -> None:
        self.__http_client = http_client

    @override
    async def buy_token(self, acc: Account, token: Token) -> bool:
        if not await self._is_token_exists(ticker=token.ticker):
            print("не сущ")
            return False

        url = self.BASE_API_URL + "/api/v5/trade/order"

        token_price = await self._get_token_price(token.ticker)
        acc_balance = await self._get_balance(acc)

        print("Цена ", token_price)

        if token_price == Decimal(0):
            return False

        print("Баланс ", acc_balance)

        payload = {
            "instId": token.ticker.instrument_id,
            "tdMode": "cash",
            "side": "buy",
            "ordType": "market",
            "px": str(token_price),
            "reduceOnly": False,
            "sz": str(int(acc_balance * Decimal(acc.use_balance_percent))),
        }

        response = await self.__http_client.post(
            url=url,
            headers=self._get_request_headers(
                acc, r_url=url, r_method="post", r_body=payload
            ),
            json=payload,
        )

        response_data = await response.json()
        print(response_data)

        if (
            response.status == 200
            and response_data["code"] == "0"
            and response_data["msg"] == ""
        ):
            return True

        return False

    async def _get_token_price(self, ticker: Ticker) -> Decimal:
        """Получить цену токена"""

        url = (
            self.BASE_API_URL
            + "/api/v5/public/mark-price"
            + f"?instId={ticker.instrument_id}"
        )

        response = await self.__http_client.get(url=url)

        if response.status != 200:
            return Decimal(0)

        response_data = await response.json()

        for r in response_data["data"]:
            if r["instId"].startswith(ticker.value):
                return Decimal(r["markPx"] or 0)

        return Decimal(0)

    async def _get_balance(self, acc: Account) -> Decimal:
        """Получить баланс аккаунта в USDT"""

        url = self.BASE_API_URL + "/api/v5/account/balance?ccy=USDT"

        response = await self.__http_client.get(
            headers=self._get_request_headers(
                acc, r_url=url, r_method="get", r_body=""
            ),
            url=url,
        )

        if response.status != 200:
            return Decimal(0)

        response_data = await response.json()

        if not (response_data["data"][0].get("details", [])):
            return Decimal(0)

        return Decimal(response_data["data"][0]["details"][0].get("eq", 0))

    async def _is_token_exists(self, *, ticker: Ticker) -> bool:
        """Проверить существует ли токен на бирже"""

        url = self.BASE_API_URL + "/api/v5/public/instruments" + "?instType=SPOT"

        response = await self.__http_client.get(url=url)

        if response.status != 200:
            return False

        response_data = await response.json()

        for token in response_data.get("data", []):
            if token.get("instId", "") == ticker.instrument_id:
                return True

        return False

    def _get_request_headers(
        self,
        acc: Account,
        *,
        r_url: str,
        r_method: str,
        r_body: dict[str, Any] | str,
    ) -> dict[str, str]:
        """Возвращает хедерсы для запроса"""

        timestamp = (
            datetime.now(timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )

        return {
            "OK-ACCESS-KEY": acc.api_key,
            "OK-ACCESS-SIGN": base64.b64encode(
                hmac.new(
                    acc.secret_key.encode("utf-8"),
                    (
                        timestamp
                        + r_method.upper()
                        + r_url.replace(self.BASE_API_URL, "")
                        + (json.dumps(r_body) if isinstance(r_body, dict) else "")
                    ).encode("utf-8"),
                    hashlib.sha256,
                ).digest()
            ).decode("utf-8"),
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": acc.passphrase,
            "Content-Type": "application/json",
            "x-simulated-trading": "1",
        }
