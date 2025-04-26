from dishka.integrations.taskiq import FromDishka, inject

from application.token import AddTokens


@inject
async def task(add_tokens: FromDishka[AddTokens]) -> None:
    print("хуй")
    await add_tokens()
