from typing import Protocol


class TransactionManager(Protocol):
    async def commit(self) -> None: ...
