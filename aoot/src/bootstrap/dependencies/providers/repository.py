from dishka import Provider, Scope, provide

from src.domain.tokens import TokenRepository

from src.infra.adapters.repositories.sqlalchemy import *
from src.infra.models import *


class SQLAlchemyRepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(SQLAlchemyTokenRepositoryImpl)


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    get_token_repo = provide(SQLAlchemyTokenRepositoryImpl, provides=TokenRepository)
