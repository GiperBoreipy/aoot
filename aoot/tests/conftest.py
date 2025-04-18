from pytest import fixture

from dishka import AsyncContainer


from infra.dependencies import get_di_container


@fixture()
def di_container() -> AsyncContainer:
    return get_di_container()
