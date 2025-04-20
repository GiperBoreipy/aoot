from typing import Protocol
from abc import abstractmethod

from domain.tokens import Ticker


class TickersInfoService(Protocol):
    @abstractmethod
    async def get_tickers(self) -> tuple[Ticker, ...]: ...
