from typing import Protocol
from abc import abstractmethod

from .entity import Token, Ticker


class TokenRepository(Protocol):
    @abstractmethod
    async def get_by_ticker(self, ticker: Ticker) -> Token | None: ...

    @abstractmethod
    async def get_all_not_buyed_tokens(self) -> tuple[Token, ...]: ...

    @abstractmethod
    async def add(self, token: Token) -> None: ...
