from dataclasses import dataclass
from typing import Final
import os
import json

from dotenv import load_dotenv


load_dotenv()


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

    @classmethod
    def get(cls) -> "Config":
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

        return cls(
            db_user=db_user,
            db_password=db_password,
            db_host=db_host,
            db_port=db_port,
            db_name=db_name,
        )


config: Final[Config] = Config.get()


@dataclass(frozen=True, slots=True, kw_only=True)
class Account:
    api_key: str
    secret_key: str
    passphrase: str
    use_balance_percent: float

    @classmethod
    def get(cls) -> tuple["Account", ...]:
        arr = []
        with open("assets/account.json", "r") as file:
            data = json.load(file)

        for acc in data["accounts"]:
            arr.append(
                cls(
                    api_key=acc["api_key"],
                    secret_key=acc["secret_key"],
                    passphrase=acc["passphrase"],
                    use_balance_percent=acc["use_balance_percent"],
                )
            )

        return tuple(arr)


accounts: Final[tuple[Account, ...]] = Account.get()
