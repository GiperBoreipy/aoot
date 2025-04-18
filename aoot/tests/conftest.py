from pytest import fixture

from dishka import AsyncContainer

from infra.dependencies import get_di_container

from bootstrap.logger import setup_logger


setup_logger(is_test=True)


@fixture()
def di_container() -> AsyncContainer:
    return get_di_container()
