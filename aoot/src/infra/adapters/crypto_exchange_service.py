from typing import override

from application.ports import CryptoExchangeService

from domain.tokens import Token

from bootstrap.configs import accounts

from infra.adapters.base import HttpClient


class OkxCryptoExchangeServiceImpl(HttpClient, CryptoExchangeService):
    @override
    async def buy_token(self, token: Token) -> bool: ...
