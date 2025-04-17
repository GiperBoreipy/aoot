from typing import Protocol, Any
from abc import abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class BaseEntity(Protocol):
    @classmethod
    @abstractmethod
    def make[T: "BaseEntity"](cls: type[T], *args: Any, **kwargs: Any) -> T: ...
