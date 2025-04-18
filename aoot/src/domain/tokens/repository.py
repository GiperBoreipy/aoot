from typing import Protocol
from abc import abstractmethod

from domain.tokens import Token


class TokenRepository(Protocol):
    @abstractmethod
    async def get_by_ticker(self, ticker: str) -> Token | None: ...

    @abstractmethod
    async def get_all_not_buyed_tokens(self) -> tuple[Token, ...]: ...

    @abstractmethod
    async def add(self, token: Token) -> None: ...
