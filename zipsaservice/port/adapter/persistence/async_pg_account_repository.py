from zipsaservice.application.repository.account_repository import AccountRepository
from zipsaservice.port.adapter.persistence.async_pg_client import AsyncPgClient
from zipsaservice.domain.model.account import Account


class AsyncPgAccountRepository(AccountRepository):

    def __init__(self, pg: AsyncPgClient) -> None:
        self._pg = pg

    async def get_account(self, id: str) -> Account:
        query = ""
        result = await self._pg.fetchrow(query=query)
        return Account.model_validate(result)

    