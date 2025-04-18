import pytest

from dishka import AsyncContainer

from infra.adapters.repositories.sqlalchemy import SQLAlchemyTokenRepositoryImpl

from application.ports import TransactionManager


@pytest.mark.asyncio
async def test_sqlalchemy_token_repo(di_container: AsyncContainer) -> None:
    async with di_container() as r_container:
        token_repo: SQLAlchemyTokenRepositoryImpl = await r_container.get(
            SQLAlchemyTokenRepositoryImpl
        )
        tm: TransactionManager = await r_container.get(TransactionManager)

        token = await token_repo.get_by_ticker("хуй")
        print(token)
        if token is None:
            return
        token.mark_as_buyed()
        await tm.commit()
        print(await token_repo.get_by_ticker("хуй"))
