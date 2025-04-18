from typing import Protocol
from abc import abstractmethod

from domain.tokens import Token


class CryptoExchangeService(Protocol):
    @abstractmethod
    async def buy_token(self, token: Token) -> bool: ...
