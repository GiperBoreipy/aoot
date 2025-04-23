from typing import Final

from dishka import Provider

from .config import Config, ConfigProvider
from .database import DatabaseProvider
from .repository import (
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    MemoryRepositoryProvider,
    TestRepositoryProvider,
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
    DatabaseProvider,
    MemoryRepositoryProvider,
    TestRepositoryProvider,
    InteractorProvider,
    AdapterProvider,
    CommonProvider,
)
