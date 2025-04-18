from typing import Final

from dishka import Provider

from .config import Config, ConfigProvider
from .database import DatabaseProvider


all_providers: Final[tuple[type[Provider], ...]] = (ConfigProvider, DatabaseProvider)
