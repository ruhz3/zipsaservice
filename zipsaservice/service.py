import click
import sys
from zipsaservice.application.repository.account_repository import AccountRepository
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
        settings = Settings(_env_file=config_path, _env_file_encoding='utf-8') # type: ignore
        pg_client = AsyncPgClient(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            db_name=settings.POSTGRES_DBNAME,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            pool_min_size=settings.POSTGRES_POOL_MIN_SIZE,
            pool_max_size=settings.POSTGRES_POOL_MAX_SIZE,
        )
        account_repository: AccountRepository = AsyncPgAccountRepository(pg=pg_client)
        zipsa_api = ZipsaAPI(
            host=settings.ZIPSA_API_HOST,
            port=settings.ZIPSA_API_PORT
        )
        zipsa_api.serve()

    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    start_service()
    