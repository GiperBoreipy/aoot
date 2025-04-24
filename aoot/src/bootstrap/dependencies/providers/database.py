from typing import AsyncIterable

from dishka import Provider, Scope, provide

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from application.ports.transaction_manager import TransactionManager

from infra.adapters import DummyTransactionManagerImpl

from bootstrap.dependencies.providers import Config


class DatabaseProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_transaction_manager(self, session: AsyncSession) -> TransactionManager:
        return session

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, factory: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        session = factory()

        yield session

        await session.close()

    @provide(scope=Scope.APP)
    async def get_session_maker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    @provide(scope=Scope.APP)
    async def get_engine(self, config: Config) -> AsyncEngine:
        return create_async_engine(config.db_url, echo=False, pool_recycle=180)


class DummyDatabaseProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_transaction_manager(self) -> TransactionManager:
        return DummyTransactionManagerImpl()
