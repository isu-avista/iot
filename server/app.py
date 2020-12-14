from avista_iot.server import IoTServer


# configuration
DEBUG = True

app = IoTServer.get_instance().app


if __name__ == '__main__':
    IoTServer.get_instance().start()
