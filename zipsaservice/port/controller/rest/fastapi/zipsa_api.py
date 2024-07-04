from contextlib import asynccontextmanager
from zipsaservice.port.adapter.persistence.async_pg_account_repository import AsyncPgAccountRepository



class ZipsaAPI:

    @asynccontextmanager
    async def lifespan(self):
        yield
    
    async def servce(self):
        pass