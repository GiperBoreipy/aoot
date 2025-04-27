from dishka import Provider, Scope, provide

from src.application.ports import *

from src.infra.adapters import *


class AdapterProvider(Provider):
    scope = Scope.REQUEST

    get_tickers_info_service = provide(
        OkxTickersInfoServiceImpl, provides=TickersInfoService
    )
    get_crypto_exchange_service = provide(
        OkxCryptoExchangeServiceImpl, provides=CryptoExchangeService
    )
