from abc import ABCMeta, abstractmethod
from zipsaservice.domain.model.user import User


class UserRepository(metaclass=ABCMeta):

    @abstractmethod
    async def get_user(self, id: str) -> User:
        pass
        