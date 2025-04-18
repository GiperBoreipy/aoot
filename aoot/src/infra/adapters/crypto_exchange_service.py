from decimal import Decimal
from typing import override, Final, Any
from datetime import datetime
import base64
import hashlib
import hmac
import json

from application.ports import CryptoExchangeService

from domain.tokens import Token

from bootstrap.configs import accounts, Account

from infra.adapters.base import HttpClient


class OkxCryptoExchangeServiceImpl(HttpClient, CryptoExchangeService):
    BASE_API_URL: Final = "https://www.okx.com"

    @override
    async def buy_token(self, token: Token) -> bool: ...

    async def _get_balance(self, account: Account) -> Decimal:
        url = self.BASE_API_URL + "/api/v5/account/balance"

    def _get_request_headers(
        self, account: Account, *, r_url: str, r_method: str, r_body: dict[str, Any]
    ) -> dict[str, str]:
        """Возвращает хедерсы для запроса"""

        timestamp = (
            datetime.now().isoformat(timespec="milliseconds").replace("+00:00", "Z")
        )

        return {
            "OK-ACCESS-KEY": account.api_key,
            "OK-ACCESS-SIGN": base64.b64encode(
                hmac.new(
                    base64.b64decode(account.secret_key),
                    (timestamp + r_method.upper() + r_url + json.dumps(r_body)).encode(
                        "utf-8"
                    ),
                    hashlib.sha256,
                ).digest()
            ).decode("utf-8"),
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": account.passphrase,
        }
