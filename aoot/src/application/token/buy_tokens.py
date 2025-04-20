from typing import override

from domain.tokens import TokenRepository

from application.ports import TransactionManager, CryptoExchangeService
from application.base import Interactor


class BuyTokens(Interactor[None, None]):
    """
    Попытатсья купить все некупленные токены
    """

    @override
    def __init__(
        self,
        token_repo: TokenRepository,
        crypto_exchange_service: CryptoExchangeService,
        transaction_manager: TransactionManager,
    ) -> None:
        self.__token_repo = token_repo
        self.__crypto_exchange_service = crypto_exchange_service
        self.__transaction_manager = transaction_manager

    @override
    async def __call__(self) -> None:
        tokens = await self.__token_repo.get_all_not_buyed_tokens()

        for token in tokens:
            buy_status = await self.__crypto_exchange_service.buy_token(token)
            if buy_status:
                token.mark_as_buyed()
                await self.__transaction_manager.commit()
