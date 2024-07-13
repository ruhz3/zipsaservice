from pydantic import BaseModel
from zipsaservice.application.authenticator import Authenticator
from zipsaservice.application.repository.account_repository import Repository
from zipsaservice.application.utils.exceptions import NoSuchAccountException, WrongPasswordException


class LoginInputDto(BaseModel):
    id: str
    password: str
    

class LoginUseCase:
    def __init__(
        self, 
        repository: Repository,
        authenticator: Authenticator
    ) -> None:
        self._repository = repository
        self._authenticator = authenticator
        
    async def execute(self, input: LoginInputDto) -> str:
        account = await self._repository.get_account(input.id)
        if not account:
            raise NoSuchAccountException
        if not self._authenticator.verify_password(input.password, account.password):
            raise WrongPasswordException
        return self._authenticator.create_access_token(account.id)
        