import pytest

from dishka import AsyncContainer

from application.ports import TickersInfoService


@pytest.mark.asyncio
async def test_tickers_info_service(di_container: AsyncContainer) -> None:
    async with di_container() as r_container:
        tickers_info_service: TickersInfoService = await r_container.get(
            TickersInfoService
        )

        print(await tickers_info_service.get_tickers())
