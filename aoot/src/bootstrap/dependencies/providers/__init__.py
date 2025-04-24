from typing import Final

from dishka import Provider

from .config import Config, ConfigProvider
from .database import DatabaseProvider, DummyDatabaseProvider
from .repository import (
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    MemoryRepositoryProvider,
    DummyRepositoryProvider,
)
from .interactors import InteractorProvider
from .adapters import AdapterProvider
from .common import CommonProvider


all_providers: Final[tuple[type[Provider], ...]] = (
    ConfigProvider,
    DatabaseProvider,
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    InteractorProvider,
    AdapterProvider,
    CommonProvider,
)

all_test_providers: Final[tuple[type[Provider], ...]] = (
    ConfigProvider,
    DummyDatabaseProvider,
    MemoryRepositoryProvider,
    DummyRepositoryProvider,
    InteractorProvider,
    AdapterProvider,
    CommonProvider,
)
