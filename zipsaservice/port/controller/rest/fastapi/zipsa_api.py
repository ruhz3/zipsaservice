from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI, APIRouter
import uvicorn
from zipsaservice.port.adapter.persistence.async_pg_account_repository import AsyncPgAccountRepository
from zipsaservice.port.controller.rest.fastapi.routes import login, accounts



class ZipsaAPI:
    server: FastAPI | Any = None

    def __init__(self, host: str, port: int):
        self._server = FastAPI()
        self._add_routes()
        self._host = host
        self._port = port
    
    def _add_routes(self) -> None:
        if self._server:
            router = APIRouter()
            router.include_router(login.router, tags=["login"])
            router.include_router(accounts.router, prefix="accounts", tags=["accounts"])
            self._server.include_router(router)

    @asynccontextmanager
    async def lifespan(self):
        yield
    
    def serve(self):
        uvicorn.run(self._server, host=self._host, port=self._port)
