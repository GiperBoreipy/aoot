from typing import override

from domain.tokens import TokenRepository

from application.ports.transaction_manager import TransactionManager
from application.base import Interactor


class BuyTokens(Interactor[None, None]):
    """
    Попытатсья купить все некупленные токены
    """

    @override
    def __init__(
        self, token_repo: TokenRepository, transaction_manager: TransactionManager
    ) -> None:
        self.__token_repo = token_repo
        self.__transaction_manager = transaction_manager

    @override
    async def __call__(self, _: None) -> None:
        tokens = await self.__token_repo.get_all_not_buyed_tokens()

        for token in tokens:
            ...
