from dataclasses import dataclass
from typing import cast, override

from domain.shared import BaseEntity


@dataclass(kw_only=True, slots=True)
class Token(BaseEntity):
    id: int

    ticker: str

    _is_buyed: bool = False

    @property
    def is_buyed(self) -> bool:
        return self._is_buyed

    def buy(self) -> None:
        self._is_buyed = True

    @classmethod
    @override
    def make(cls, ticker: str) -> "Token":
        return cls(id=cast(int, None), ticker=ticker)
