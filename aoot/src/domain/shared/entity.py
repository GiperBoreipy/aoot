from typing import Protocol, Any
from abc import abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True)
class BaseEntity(Protocol):
    @classmethod
    @abstractmethod
    def new[T: "BaseEntity"](cls: type[T], *args: Any, **kwargs: Any) -> T: ...
