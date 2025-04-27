from typing import override, Final
import asyncio

from aiohttp import ClientSession

from parsel import Selector

from src.application.ports import TickersInfoService

from src.domain.tokens import Ticker


class OkxTickersInfoServiceImpl(TickersInfoService):
    DOMAIN: Final[str] = "https://www.okx.com"
    BASE_URL: Final[str] = DOMAIN + "/ru/help/section/announcements-new-listings"

    def __init__(self, client: ClientSession) -> None:
        self._client = client

    @override
    async def get_tickers(self) -> tuple[Ticker, ...]:
        while True:
            try:
                res = await self._get_tickers()
                if res:
                    break
            except Exception:
                await asyncio.sleep(2)
        return tuple(set(res))

    async def _get_tickers(self) -> tuple[Ticker, ...]:
        urls = []

        selector = await self.__get_selector(f"{self.BASE_URL}/page/1")
        last_page = self.__extract_last_page_number(selector)

        urls.extend(self.__extract_page_urls(selector))

        selectors = await asyncio.gather(
            *[
                self.__get_selector(f"{self.BASE_URL}/page/{page_id}")
                for page_id in range(2, last_page + 1)
            ]
        )

        for selector in selectors:
            urls.extend(self.__extract_page_urls(selector))

        selectors = await asyncio.gather(*[self.__get_selector(url) for url in urls])

        tickers = []

        for selector in selectors:
            ticker = selector.re_first(r"Тикер: ([A-Z]*)")

            if ticker:
                tickers.append(Ticker(ticker))

        return tuple(tickers)

    async def __get_selector(self, url: str) -> Selector:
        response = await self._client.get(url)

        text = await response.text()

        selector = Selector(text)

        return selector

    def __extract_last_page_number(self, selector: Selector) -> int:
        page_texts = selector.css("a.okui-pagination-item-link::text").getall()

        if not page_texts:
            raise ValueError("Page texts is empty.")

        last_page_text = page_texts[-1]

        if not last_page_text.isdigit():
            raise ValueError(f"Can't cast {last_page_text} to int")

        return int(last_page_text)

    def __extract_page_urls(self, selector: Selector) -> list[str]:
        return [
            self.DOMAIN + path
            for path in selector.css(
                'a.index_articleLink__Z6ycB::attr("href")'
            ).getall()
        ]
