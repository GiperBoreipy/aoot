from typing import override

from sqlalchemy import select

from domain.tokens import TokenRepository, Token

from infra.repositories.sqlalchemy.base import SQLAlchemyBaseRepository


class SQLAlchemyTokenRepositoryImpl(SQLAlchemyBaseRepository, TokenRepository):
    @override
    async def get_by_ticker(self, ticker: str) -> Token | None:
        stmt = select(Token).where(Token.ticker == ticker)  # type: ignore

        result = await self._session.scalar(stmt)

        return result

    @override
    async def get_all_not_buyed_tokens(self) -> tuple[Token, ...]:
        stmt = select(Token).where(Token.is_buyed == False)  # type: ignore

        results = await self._session.scalars(stmt)

        return tuple(results)

    @override
    async def add(self, token: Token) -> None:
        self._session.add(token)

        await self._session.flush()
