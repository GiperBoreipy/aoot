from dataclasses import dataclass, field

from .vo import Ticker


@dataclass(kw_only=True)
class Token:
    id: int = field(init=False, default=0)

    ticker: Ticker

    _is_buyed: bool = field(init=False, default=False)

    @property
    def is_buyed(self) -> bool:
        return self._is_buyed

    def mark_as_buyed(self) -> None:
        self._is_buyed = True
