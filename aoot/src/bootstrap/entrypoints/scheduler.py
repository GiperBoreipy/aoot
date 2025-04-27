from taskiq import InMemoryBroker, TaskiqScheduler, async_shared_broker
from taskiq.schedule_sources import LabelScheduleSource

from dishka.integrations.taskiq import setup_dishka

from src.bootstrap.dependencies import get_di_container
from src.bootstrap.logger import setup_logger
from src.infra.tasks import tasks


setup_logger()


broker = InMemoryBroker()
async_shared_broker.default_broker(broker)


scheduler = TaskiqScheduler(broker, [LabelScheduleSource(async_shared_broker)])


container = get_di_container()
setup_dishka(container, broker)
