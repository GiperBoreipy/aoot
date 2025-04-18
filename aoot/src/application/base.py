from typing import Protocol, Any
from abc import abstractmethod


class Interactor[TReq: Any, TRes: Any](Protocol):
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    @abstractmethod
    async def __call__(self, request: TReq) -> TRes: ...
