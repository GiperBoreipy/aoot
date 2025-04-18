from typing import Protocol, Any
from abc import abstractmethod


class TransactionManager(Protocol):
    @abstractmethod
    async def commit(self, *args: Any, **kwargs: Any) -> None: ...
