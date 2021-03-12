from avista_iot import api
from avista_base.service import Service
# from multiprocessing import Process


class IoTServer(Service):

    def __init__(self):
        """ instantiate the app """
        super().__init__()
        self.sensor_sweep = None

    def _setup_endpoints(self):
        super()._setup_endpoints()
        self._app.register_blueprint(api.api_bp)

    def start(self):
        super().start()
        # self._app.session = avista_data.database.db
        # self._proc = Process(target=self._app.run, kwargs={'host': self.hostname, 'port': self.port})
        # self._proc.start()

    def check_status(self):
        pass
