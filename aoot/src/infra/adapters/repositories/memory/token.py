from typing import override

from domain.tokens import TokenRepository, Token


class MemoryTokenRepositoryImpl(TokenRepository):
    def __init__(self) -> None:
        self.__items: list[Token] = []

    @override
    async def get_by_ticker(self, ticker: str) -> Token | None:
        for token in self.__items:
            if token.ticker == ticker:
                return token

    @override
    async def get_all_not_buyed_tokens(self) -> tuple[Token, ...]:
        return tuple(i for i in self.__items if not i.is_buyed)

    @override
    async def add(self, token: Token) -> None:
        self.__items.append(token)
