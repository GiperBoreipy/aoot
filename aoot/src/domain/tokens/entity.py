from dataclasses import dataclass
from typing import cast, override

from domain.shared import BaseEntity


type Ticker = str


@dataclass(kw_only=True)
class Token(BaseEntity):
    id: int

    ticker: Ticker

    _is_buyed: bool = False

    @property
    def is_buyed(self) -> bool:
        return self._is_buyed

    def mark_as_buyed(self) -> None:
        self._is_buyed = True

    @classmethod
    @override
    def new(cls, ticker: Ticker) -> "Token":
        return cls(id=cast(int, None), ticker=ticker)
