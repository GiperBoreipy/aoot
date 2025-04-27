from dishka import Provider

from .database import DatabaseProvider, DummyDatabaseProvider
from .repository import (
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
)
from .interactors import InteractorProvider
from .adapters import AdapterProvider
from .common import CommonProvider


all_providers: tuple[type[Provider], ...] = (
    DatabaseProvider,
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    InteractorProvider,
    AdapterProvider,
    CommonProvider,
)

all_test_providers: tuple[type[Provider], ...] = (
    DummyDatabaseProvider,
    InteractorProvider,
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    AdapterProvider,
    CommonProvider,
)
