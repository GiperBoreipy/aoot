import asyncio

from aiohttp import ClientSession


class HttpClient:
    def __init__(self) -> None:
        self._client = ClientSession()

    def __del__(self) -> None:
        asyncio.get_event_loop().create_task(self._client.close())
