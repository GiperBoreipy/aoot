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

        return cls(
            db_user=db_user or "default_postgres_user",
            db_password=db_password or "default_postgres_password",
            db_host=db_host or "postgres",
            db_port=db_port or 5432,
            db_name=db_name or "default_postgres_db",
        )


config: Final[Config] = Config.get()


@dataclass(frozen=True, slots=True, kw_only=True)
class Account:
    api_key: str
    secret_key: str
    passphrase: str
    use_balance_percent: float

    @classmethod
    def get(cls) -> "Account":
        arr: list["Account"] = []
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

        return arr[0]


account: Final[Account] = Account.get()
