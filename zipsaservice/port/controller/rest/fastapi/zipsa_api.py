from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI
import uvicorn
from zipsaservice.port.adapter.persistence.async_pg_account_repository import AsyncPgAccountRepository



class ZipsaAPI:
    server: FastAPI | Any = None

    @asynccontextmanager
    async def lifespan(self):
        yield
    
    async def serve(self, config, host, port):
        self._config = config
        uvicorn.run(self.server, host=host, port=port)
