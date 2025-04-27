from typing import override

from src.application.ports import TransactionManager


class DummyTransactionManagerImpl(TransactionManager):
    @override
    async def commit(self) -> None:
        pass
