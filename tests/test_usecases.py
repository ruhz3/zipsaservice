import asyncio
import pytest

pytest_plugins = ('pytest_asyncio',)


@pytest.mark.asyncio
async def test_login(account_repository, authenticator):
    await asyncio.sleep(0.5)
