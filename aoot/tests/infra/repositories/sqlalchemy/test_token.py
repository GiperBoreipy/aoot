import pytest

from dishka import AsyncContainer

from domain.ports.transaction_manager import TransactionManager

from infra.repositories.sqlalchemy import SQLAlchemyTokenRepositoryImpl


@pytest.mark.asyncio
async def test_sqlalchemy_token_repo(di_container: AsyncContainer) -> None:
    async with di_container() as r_container:
        token_repo: SQLAlchemyTokenRepositoryImpl = await r_container.get(
            SQLAlchemyTokenRepositoryImpl
        )
        transaction_manager: TransactionManager = await r_container.get(
            TransactionManager
        )

        print(transaction_manager)

        print(token_repo)
