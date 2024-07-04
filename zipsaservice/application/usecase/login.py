from pydantic import BaseModel
from zipsaservice.application.authenticator import Authenticator
from zipsaservice.application.repository.account_repository import AccountRepository
from zipsaservice.application.utils.exceptions import NoSuchAccountException, WrongPasswordException
from zipsaservice.domain.model.user import User


class LoginInputDto(BaseModel):
    id: str
    password: str
    

class LoginUseCase:
    def __init__(
        self, 
        account_repository: AccountRepository,
        authenticator: Authenticator
    ) -> None:
        self._account_repository = account_repository
        self._authenticator = authenticator
        
    async def execute(self, input: LoginInputDto) -> str:
        account = await self._account_repository.get_account(input.id)
        if not account:
            raise NoSuchAccountException
        if not self._authenticator.verify_password(input.password, account.password):
            raise WrongPasswordException
        return self._authenticator.create_access_token(account.id)
        