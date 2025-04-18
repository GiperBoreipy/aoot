from dishka import Provider, Scope, provide

from domain.tokens import TokenRepository

from infra.repositories.sqlalchemy import *


class SQLAlchemyRepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(SQLAlchemyTokenRepositoryImpl)


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(SQLAlchemyTokenRepositoryImpl, provides=TokenRepository)
