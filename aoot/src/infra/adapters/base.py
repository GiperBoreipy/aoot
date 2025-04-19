import asyncio

from aiohttp import ClientSession


class HttpClient(ClientSession):
    def __del__(self) -> None:
        asyncio.get_event_loop().create_task(self.close())
