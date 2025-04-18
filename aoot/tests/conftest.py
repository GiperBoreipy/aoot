from pytest import fixture

from dishka import AsyncContainer

from bootstrap.dependencies import get_di_container
from bootstrap.logger import setup_logger
from infra.models import *


setup_logger(is_test=True)


@fixture()
def di_container() -> AsyncContainer:
    return get_di_container()
