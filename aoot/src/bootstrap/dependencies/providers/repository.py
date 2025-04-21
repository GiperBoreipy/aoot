from dishka import Provider, Scope, provide

from domain.tokens import TokenRepository

from infra.adapters.repositories.sqlalchemy import *
from infra.adapters.repositories.memory import *


class MemoryRepositoryProvider(Provider):
    scoep = Scope.REQUEST

    get_token_repo = provide(MemoryTokenRepositoryImpl)


class SQLAlchemyRepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(SQLAlchemyTokenRepositoryImpl)


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(SQLAlchemyTokenRepositoryImpl, provides=TokenRepository)


class TestRepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(MemoryTokenRepositoryImpl, provides=TokenRepository)
