from dataclasses import dataclass
from typing import cast, override

from domain.shared import BaseEntity


@dataclass(kw_only=True, slots=True)
class Token(BaseEntity):
    id: int

    ticker: str

    is_buyed: bool

    @classmethod
    @override
    def make(cls, ticker: str) -> "Token":
        return cls(id=cast(int, None), ticker=ticker, is_buyed=False)
