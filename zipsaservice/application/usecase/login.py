from pydantic import BaseModel
from zipsaservice.application.repository.user_repository import UserRepository
from zipsaservice.application.repository.account_repository import AccountRepository
from zipsaservice.domain.exception.exceptions import LoginFailedException
from zipsaservice.domain.model.user import User


class LoginInputDto(BaseModel):
    id: str
    password: str


class LoginUseCase:
    def __init__(
        self, 
        account_repository: AccountRepository,
        user_repository: UserRepository
    ) -> None:
        self._account_repository = account_repository
        self._user_repository = user_repository

    async def execute(self, input: LoginInputDto):
        pass
