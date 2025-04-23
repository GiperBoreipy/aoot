import pytest

from dishka import AsyncContainer

from application.ports import CryptoExchangeService

from infra.adapters import OkxCryptoExchangeServiceImpl

from bootstrap.configs import accounts


@pytest.mark.asyncio
async def test_crypto_exchange_service(di_container: AsyncContainer) -> None:
    async with di_container() as r_container:
        crypto_exchange_service: OkxCryptoExchangeServiceImpl = await r_container.get(
            CryptoExchangeService
        )

        print(
            await crypto_exchange_service._is_token_exists(accounts[0], ticker="PROMPT")
        )
