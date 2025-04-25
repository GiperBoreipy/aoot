from typing import override

from domain.tokens import TokenRepository, Token

from application.ports import TransactionManager, TickersInfoService
from application.base import Interactor


class AddTokens(Interactor[str, None]):
    @override
    def __init__(
        self,
        token_repo: TokenRepository,
        ticker_info_service: TickersInfoService,
        transaction_manager: TransactionManager,
    ) -> None:
        self.__token_repo = token_repo
        self.__tickers_info_service = ticker_info_service
        self.__transaction_manager = transaction_manager

    @override
    async def __call__(self) -> None:
        for ticker in await self.__tickers_info_service.get_tickers():
            token = Token(ticker=ticker)

            await self.__token_repo.add(token)

            await self.__transaction_manager.commit()
