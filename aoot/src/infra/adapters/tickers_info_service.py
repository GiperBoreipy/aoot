from typing import override

from application.ports import TickersInfoService

from domain.tokens import Ticker


class OkxTickersInfoServiceImpl(TickersInfoService):
    @override
    async def get_tickers(self) -> tuple[Ticker, ...]: ...
