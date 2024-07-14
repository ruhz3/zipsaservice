from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI, APIRouter
import uvicorn
from zipsaservice.application.usecase.use_cases import UseCases
from zipsaservice.application.usecase.login import LoginInputDto


def route(method: str, path: str):
    def decorator(func):
        func._route_info = {"path": path, "methods": [method]}
        return func
    return decorator


class ZipsaAPI:

    def __init__(self, use_cases: UseCases):
        self.server = FastAPI()
        self._use_cases = use_cases
        self._add_routes()
    
    def _add_routes(self):
        router = APIRouter()
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, "_route_info"):
                route_info = attr._route_info
                router.add_api_route(route_info["path"], attr, methods=route_info["methods"])          
        self.server.include_router(router)
    
    def serve(self, host: str, port: int,):
        uvicorn.run(self.server, host=host, port=port)
    
    @property
    def use_cases(self):
        return self._use_cases
    
    @route("POST", "/login/access-token")
    async def login_access_token(self, input: LoginInputDto):
        return self._use_cases.login.execute(input)
    
    
