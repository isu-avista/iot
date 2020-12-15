from avista_iot import api
from avista_base.service import Service


class IoTServer(Service):

    def __init__(self):
        """ instantiate the app """
        super().__init__()

    def _setup_endpoints(self):
        self._app.register_blueprint(api.api_bp)

    def start(self):
        """ starts the server """
        super().start()
        # this is where to add access to the ProcessorManager()

    def stop(self):
        """ Stops the server """
        super().stop()
        # Also need to kill the ProcessorManager() here

    def check_status(self):
        pass
