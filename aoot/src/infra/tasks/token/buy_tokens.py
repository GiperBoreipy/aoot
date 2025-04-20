from dishka.integrations.taskiq import FromDishka, inject

from application.token import BuyTokens


@inject
async def task(buy_tokens: FromDishka[BuyTokens]) -> None:
    await buy_tokens()
