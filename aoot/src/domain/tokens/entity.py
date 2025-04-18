from dataclasses import dataclass
from typing import cast, override

from domain.shared import BaseEntity


@dataclass(kw_only=True)
class Token(BaseEntity):
    id: int

    ticker: str

    _is_buyed: bool = False

    @property
    def is_buyed(self) -> bool:
        return self._is_buyed

    def mark_as_buyed(self) -> None:
        self._is_buyed = True

    @classmethod
    @override
    def new(cls, ticker: str) -> "Token":
        return cls(id=cast(int, None), ticker=ticker)
