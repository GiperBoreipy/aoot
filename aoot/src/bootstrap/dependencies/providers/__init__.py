from typing import Final

from dishka import Provider

from .config import Config, ConfigProvider
from .database import DatabaseProvider
from .repository import SQLAlchemyRepositoryProvider, RepositoryProvider
from .interactors import InteractorProvider


all_providers: Final[tuple[type[Provider], ...]] = (
    ConfigProvider,
    DatabaseProvider,
    SQLAlchemyRepositoryProvider,
    RepositoryProvider,
    InteractorProvider,
)
