from dataclasses import dataclass
import os

from dishka import Provider, Scope, provide

from dotenv import load_dotenv


@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def get_config(self) -> Config:
        load_dotenv()

        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")

        if (
            db_user is None
            or db_password is None
            or db_host is None
            or db_port is None
            or db_name is None
        ):
            raise KeyError("Переменные окружения не найдены")

        return Config(
            db_user=db_user,
            db_password=db_password,
            db_host=db_host,
            db_port=db_port,
            db_name=db_name,
        )
