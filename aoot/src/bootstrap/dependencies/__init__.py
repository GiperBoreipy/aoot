from dishka import AsyncContainer, make_async_container

from .providers import all_providers, all_test_providers


def get_di_container() -> AsyncContainer:
    container = make_async_container(*[_() for _ in all_providers])
    return container


def get_test_di_container() -> AsyncContainer:
    container = make_async_container(*[_() for _ in all_test_providers])
    return container
