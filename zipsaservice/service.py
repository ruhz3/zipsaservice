import click
import sys
from zipsaservice.port.controller.rest.fastapi.zipsa_api import ZipsaAPI


@click.group()
def service():
    pass


@service.command("start")
@click.option('-b', '--bind', 'host', default='0.0.0.0')
def start_service():
    try:
        conf = None
        api = ZipsaAPI()
    except:
        sys.exit(1)
