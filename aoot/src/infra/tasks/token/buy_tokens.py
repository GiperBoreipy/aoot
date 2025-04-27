from taskiq.brokers.shared_broker import shared_task

from dishka.integrations.taskiq import FromDishka, inject

from src.application.token import BuyTokens


@shared_task("schedule_task_buy_tokens", schedule=[{"cron": "*/1 * * * *", "args": []}])
@inject
async def task(buy_tokens: FromDishka[BuyTokens]) -> None:
    await buy_tokens()
