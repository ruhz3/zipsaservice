from contextlib import asynccontextmanager


class ZipsaAPI:

    @asynccontextmanager
    async def lifespan(self):
        yield
        