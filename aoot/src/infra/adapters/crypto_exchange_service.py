from typing import override

from application.ports import CryptoExchangeService

from domain.tokens import Token

from bootstrap.configs import accounts


class OkxCryptoExchangeServiceImpl(CryptoExchangeService):
    def __init__(self) -> None: ...

    @override
    async def buy_token(self, token: Token) -> bool: ...
