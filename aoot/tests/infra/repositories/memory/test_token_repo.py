import pytest

from dishka import AsyncContainer

from domain.tokens import Token, Ticker

from infra.adapters.repositories.memory import MemoryTokenRepositoryImpl

from application.ports import TransactionManager


@pytest.mark.asyncio
async def test_get_add_token(di_container: AsyncContainer) -> None:
    async with di_container() as r_container:
        token_repo = await r_container.get(MemoryTokenRepositoryImpl)
        tm = await r_container.get(TransactionManager)

        token = Token(ticker=Ticker("науй ты смотришь"))
        assert token.id == 0
        await token_repo.add(token)
        await tm.commit()
        assert token.id != 0
