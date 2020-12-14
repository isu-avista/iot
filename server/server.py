import avista_data as data
from avista_data import db
from avista_base import config as conf
from flask import Flask
from flask_cors import CORS
from pathlib import Path
import config
import os
import logging


class IoTServer:

    def __init__(self):
        # instantiate the app
        self.app = Flask(__name__)
        self.app.config.from_object(config.Config())
        self.config = {}
        self.configfile = Path(os.getcwd()) / "conf" / "config.yml"
        self.logfile = Path(os.getcwd()) / "logs" / "server.log"

        # enable CORS
        CORS(self.app, resources={r'/*': {'origins': '*'}})

        data.init(self.app)

    def start(self):
        logging.basicConfig(filename=self.logfile, level=logging.DEBUG)
        conf.load(self.configfile)
        self.app.run(port=5000)

    def get_config(self, section):
        return self.config[section]

    def set_config(self, section, config_data):
        self.config[section] = config_data
        conf.save(self.config, self.configfile)

    def check_status(self):
        pass

    def get_log(self):
        with open(self.logfile, "r") as a_file:
            lines = a_file.readlines()
            return dict(log='\n'.join(lines[-5:]))
