from typing import Protocol
from abc import abstractmethod

from src.domain.tokens import Token

from src.bootstrap.configs import Account


class CryptoExchangeService(Protocol):
    @abstractmethod
    async def buy_token(self, acc: Account, token: Token) -> bool: ...
