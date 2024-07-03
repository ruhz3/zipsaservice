from abc import ABCMeta, abstractmethod


class AccountRepository(metaclass=ABCMeta):

    @abstractmethod
    async def get_password(self, id: str) -> str:
        pass
        