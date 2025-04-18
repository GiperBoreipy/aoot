from typing import override

from sqlalchemy import select

from domain.tokens import TokenRepository, Token

from infra.repositories.sqlalchemy.base import SQLAlchemyBaseRepository
from infra.models import TOKENS_TABLE


class SQLAlchemyTokenRepositoryImpl(SQLAlchemyBaseRepository, TokenRepository):
    @override
    async def get_by_ticker(self, ticker: str) -> Token | None:
        stmt = select(TOKENS_TABLE).where(TOKENS_TABLE.c.ticker == ticker)

        result = await self._session.execute(stmt)
        row = result.fetchone()

        if row is None:
            return None

        print(row, type(row))

    @override
    async def get_all_not_buyed_tokens(self) -> tuple[Token, ...]: ...

    @override
    async def add(self, token: Token) -> None:
        self._session.add(token)

        await self._session.flush()
