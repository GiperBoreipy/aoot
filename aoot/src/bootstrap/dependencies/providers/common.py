from dishka import Provider, Scope, provide

from aiohttp import ClientSession

from src.infra.adapters.base import HttpClient


class CommonProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_http_client(self) -> HttpClient:
        return ClientSession()
