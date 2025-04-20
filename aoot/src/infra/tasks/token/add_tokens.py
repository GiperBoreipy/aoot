from dishka.integrations.taskiq import FromDishka, inject

from application.token import AddTokens


@inject
async def task(add_tokens: FromDishka[AddTokens]) -> None:
    await add_tokens()
