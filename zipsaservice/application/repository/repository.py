from zipsaservice.application.repository.account_repository import AccountRepository


class Repository:

    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository

    def __getattr__(self, method):
        if hasattr(self._account_repository, method):
            return getattr(self.account_repository, method)
        