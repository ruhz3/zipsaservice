from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI
import uvicorn
from zipsaservice.application.usecase.use_cases import UseCases
from zipsaservice.application.usecase.login import LoginInputDto


class ZipsaAPI:

    def __init__(self, host: str, port: int, use_cases: UseCases):
        self.server = FastAPI()
        self._use_cases = use_cases
        self._host = host
        self._port = port
    
    @asynccontextmanager
    async def lifespan(self):
        yield
    
    def serve(self):
        uvicorn.run(self._server, host=self._host, port=self._port)
    
    @property
    def use_cases(self):
        return self._use_cases


app = ZipsaAPI()
api = ZipsaAPI().server


@api.post("/login/access-token")
async def login_access_token(input: LoginInputDto):
    return app.use_cases.login.execute(input)

