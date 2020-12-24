from avista_iot import api
from avista_base.service import Service
from avista_sensors.processor_manager import ProcessorManager


class IoTServer(Service):

    def __init__(self):
        """ instantiate the app """
        super().__init__()
        self.processor_manager = None

    def _setup_endpoints(self):
        super()._setup_endpoints()
        self._app.register_blueprint(api.api_bp)
        self.processor_manager = ProcessorManager(self._app, self._config)
        self.processor_manager.init()

    def start(self):
        """ starts the server """
        super().start()
        self.processor_manager.run()
        # this is where to add access to the ProcessorManager()

    def stop(self):
        """ Stops the server """
        super().stop()
        self.processor_manager.stop()
        # Also need to kill the ProcessorManager() here

    def check_status(self):
        pass
