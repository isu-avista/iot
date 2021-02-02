from dotenv import load_dotenv

from avista_iot.server import IoTServer
from pathlib import Path
import os

# configuration
DEBUG = True

path = Path(os.getcwd()) / ".flaskenv"
if path.exists():
    load_dotenv(path)

IoTServer.get_instance().init()

app = IoTServer.get_instance()._app

if __name__ == '__main__':
    IoTServer.get_instance().start()
