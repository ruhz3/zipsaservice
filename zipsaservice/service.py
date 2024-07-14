import click
import sys
from zipsaservice.application.authenticator import Authenticator
from zipsaservice.application.repository.account_repository import AccountRepository
from zipsaservice.application.repository.repository import Repository
from zipsaservice.application.usecase.use_cases import UseCases
from zipsaservice.application.utils.config import Settings
from zipsaservice.port.controller.rest.fastapi.zipsa_api import ZipsaAPI
from zipsaservice.port.adapter.persistence.async_pg_account_repository import AsyncPgAccountRepository
from zipsaservice.port.adapter.persistence.async_pg_client import AsyncPgClient


@click.group()
def service():
    pass


@service.command("start")
@click.option('-c', '--config', 'config_path', default='/root/app/manifests/service.env')
def start_service(config_path: str):
    try:
        # 00. config 를 불러온다. 
        settings = Settings(_env_file=config_path, _env_file_encoding='utf-8') # type: ignore

        # 01. repository를 초기화한다. 
        pg_client = AsyncPgClient(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            db_name=settings.POSTGRES_DBNAME,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            pool_min_size=settings.POSTGRES_POOL_MIN_SIZE,
            pool_max_size=settings.POSTGRES_POOL_MAX_SIZE,
        )
        repository = Repository(
            account_repository=AsyncPgAccountRepository(pg=pg_client)
        )

        # 02. authenticator를 초기화한다. 
        authenticator=Authenticator(
            crypt_algorithm=settings.CRYPT_ALGORITHM,
            hash_algorithm=settings.HASH_ALGORITHM,
            token_expire_min=settings.TOKEN_EXPIRE_TIMEDELTA
        )

        # 03. usecase를 초기화한다. 
        use_cases = UseCases(
            authenticator=authenticator,
            repository=repository
        )

        # 04. fastapi를 초기화하고 수행한다. 
        ZipsaAPI(use_cases).serve(
            host=settings.ZIPSA_API_HOST,
            port=settings.ZIPSA_API_PORT
        )

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    start_service()
    