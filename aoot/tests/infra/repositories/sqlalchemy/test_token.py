import pytest

from dishka import AsyncContainer

from infra.repositories.sqlalchemy import SQLAlchemyTokenRepositoryImpl


@pytest.mark.asyncio
async def test_sqlalchemy_token_repo(di_container: AsyncContainer) -> None:
    async with di_container() as r_container:
        token_repo: SQLAlchemyTokenRepositoryImpl = await r_container.get(
            SQLAlchemyTokenRepositoryImpl
        )

        print(await token_repo.get_by_ticker("хуй"))
        print(await token_repo.get_by_ticker("hui"))
