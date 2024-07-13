from zipsaservice.application.authenticator import Authenticator
from zipsaservice.application.repository.repository import Repository
from zipsaservice.application.usecase import (
    login
)


class UseCases:
    def __init__(self, authenticator: Authenticator, repository: Repository) -> None:
        self._authenticator = authenticator
        self._repository = repository
        self.__add_usecases()

    def __add_usecases(self):
        self.login = login.LoginUseCase(repository=self._repository, authenticator=self._authenticator)

        