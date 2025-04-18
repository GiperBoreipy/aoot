from typing import override

from domain.tokens import TokenRepository, Token

from application.ports import TransactionManager
from application.base import Interactor


class AddToken(Interactor[str, None]):
    @override
    def __init__(
        self, token_repo: TokenRepository, transaction_manager: TransactionManager
    ) -> None:
        self.__token_repo = token_repo
        self.__transaction_manager = transaction_manager

    @override
    async def __call__(self, request: str) -> None:
        """request - ticker"""

        token = Token.new(ticker=request)

        await self.__token_repo.add(token)

        await self.__transaction_manager.commit()
