from abc import ABCMeta, abstractmethod
from domain.model.account import Account


class AccountRepository(metaclass=ABCMeta):

    @abstractmethod
    async def get_account(self, id: str) -> Account:
        pass
        