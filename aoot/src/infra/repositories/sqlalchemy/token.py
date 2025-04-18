from typing import override

from domain.tokens import TokenRepository, Token

from infra.repositories.sqlalchemy.base import SQLAlchemyBaseRepository


class SQLAlchemyTokenRepositoryImpl(SQLAlchemyBaseRepository, TokenRepository):
    @override
    async def get_by_ticker(self, ticker: str) -> Token | None: ...

    @override
    async def get_all_not_buyed_tokens(self) -> tuple[Token, ...]: ...
