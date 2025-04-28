from typing import override
import logging

from src.domain.tokens import TokenRepository, Token

from src.application.ports import TransactionManager, TickersInfoService
from src.application.base import Interactor


logger = logging.getLogger(__name__)


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
            if (await self.__token_repo.get_by_ticker(ticker)) is not None:
                return

            token = Token(ticker=ticker)

            await self.__token_repo.add(token)

            await self.__transaction_manager.commit()
