from taskiq.brokers.shared_broker import shared_task

from dishka.integrations.taskiq import FromDishka, inject

from src.application.token import AddTokens


@shared_task("schedule_task_add_tokens", schedule=[{"cron": "*/1 * * * *", "args": []}])
@inject
async def task(add_tokens: FromDishka[AddTokens]) -> None:
    print("писюн")
    await add_tokens()
