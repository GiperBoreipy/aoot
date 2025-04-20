from typing import Final, Callable, Coroutine, Any

from .token import add_tokens_task, buy_tokens_task


tasks: Final[tuple[Callable[[], Coroutine[Any, Any, Any]], ...]] = (
    add_tokens_task,
    buy_tokens_task,
)
