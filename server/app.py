from dotenv import load_dotenv

from avista_iot.server import IoTServer
from avista_base.avista_app import AvistaApp
from pathlib import Path
import os

# configuration
DEBUG = True

path = Path(os.getcwd()) / ".flaskenv"
if path.exists():
    load_dotenv(path)

if __name__ == '__main__':
    service = IoTServer.get_instance()
    service.initialize()
    service.start()
    app = service.get_app()

    options = dict(
        bind=service.get_hostname() + ":" + service.get_port(),
        workers=1
    )

    AvistaApp(app, options).run()

