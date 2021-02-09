from dotenv import load_dotenv

from avista_iot.server import IoTServer
from pathlib import Path
import os

# configuration
DEBUG = True

path = Path(os.getcwd()) / ".flaskenv"
if path.exists():
    load_dotenv(path)

if __name__ == '__main__':
    options = {
        'bind': '0.0.0.0:5000',
        'workers': 1,
    }

    IoTServer(options).get_instance().start()
