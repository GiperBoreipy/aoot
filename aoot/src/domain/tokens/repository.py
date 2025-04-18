from typing import Protocol
from abc import abstractmethod

from domain.tokens import Token


class TokenRepository(Protocol):
    @abstractmethod
    async def get_by_ticker(self, ticker: str) -> Token | None: ...
