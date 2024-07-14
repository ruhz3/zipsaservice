from typing import Any
import asyncpg


class AsyncPgClient:
    
    def __init__(
        self,
        host: str,
        port: int,
        db_name: str,
        user: str,
        password: str,
        pool_min_size: int,
        pool_max_size: int
    ) -> None:
        self._host = host
        self._port = port
        self._db_name = db_name
        self._user = user
        self._password = password
        self._pool_min_size = pool_min_size
        self._pool_max_size = pool_max_size
        self._connection_pool: asyncpg.Pool | Any = None

    async def open(self):
        await self.close()
        self._connection_pool = asyncpg.create_pool(
            host=self._host,
            port=self._port,
            database=self._db_name,
            user=self._user,
            password=self._password,
            min_size=self._pool_min_size,
            max_size=self._pool_max_size
        )

    async def close(self):
        if self._connection_pool:
            await self._connection_pool.close()
        self._connection_pool = None

    async def fetch(self, query: str, *args):
        async with self._connection_pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def fetchrow(self, query: str, *args):
        pass

    async def execute(self, query: str, *args):
        pass