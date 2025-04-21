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


all_providers: Final[tuple[type[Provider], ...]] = (
    ConfigProvider,
    DatabaseProvider,
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    InteractorProvider,
)

all_test_providers: Final[tuple[type[Provider], ...]] = (
    ConfigProvider,
    DatabaseProvider,
    MemoryRepositoryProvider,
    TestRepositoryProvider,
    InteractorProvider,
)
