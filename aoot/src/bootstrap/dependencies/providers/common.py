from typing import AsyncIterable

from dishka import Provider, Scope, provide

from aiohttp import ClientSession


class CommonProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_http_client(self) -> AsyncIterable[ClientSession]:
        async with ClientSession() as session:
            yield session
