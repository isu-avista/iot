from avista_iot import api
from avista_base.service import Service
from avista_sensors.sensor_sweep import SensorSweep


class IoTServer(Service):

    def __init__(self):
        """ instantiate the app """
        super().__init__()
        self.sensor_sweep = None

    def _setup_endpoints(self):
        super()._setup_endpoints()
        self._app.register_blueprint(api.api_bp)
        self.sensor_sweep = SensorSweep(self._app, self._config)
        self.sensor_sweep.init()

    def start(self):
        """ starts the server """
        super().initialize()
        # Initialize calls _setup_endpoints which creates the sensor_sweep
        # then run the SensorSweep on a thread and then start the rest of the server
        self.sensor_sweep.run()
        super().start()

    def stop(self):
        """ Stops the server """
        super().stop()
        self.sensor_sweep.stop()

    def check_status(self):
        pass
