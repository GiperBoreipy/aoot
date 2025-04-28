from typing import override

from src.domain.tokens import TokenRepository

from src.application.ports import TransactionManager, CryptoExchangeService
from src.application.base import Interactor

from src.bootstrap.configs import account


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
            buy_status = await self.__crypto_exchange_service.buy_token(account, token)
            print(buy_status)
            if buy_status:
                token.mark_as_buyed()
                await self.__transaction_manager.commit()
