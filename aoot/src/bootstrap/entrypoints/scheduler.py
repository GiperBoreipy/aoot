from taskiq import InMemoryBroker, TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource

from dishka.integrations.taskiq import setup_dishka

from infra.tasks import tasks

from bootstrap.dependencies import get_di_container


def main() -> None:
    broker = InMemoryBroker()
    scheduler = TaskiqScheduler(broker, [LabelScheduleSource(broker)])

    for task in tasks:
        task_name = f"shedule_{task.__qualname__}"
        broker.register_task(
            task, task_name=task_name, schedule=[{"time": "*/10 * * * * *", "args": []}]
        )

    container = get_di_container()

    setup_dishka(container, broker)


if __name__ == "__main__":
    main()
