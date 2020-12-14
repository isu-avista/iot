import unittest
from tests.api.base_api_test import BaseApiTest


class MonitorTest(BaseApiTest):

    def test_status(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", "/monitor/status")
        print(rv.get_json())
        self.fail()

    def test_status_noauth(self):
        self.fail()

    def test_sensors(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", "/monitor/sensors")
        print(rv.get_json())
        self.fail()

    def test_sensors_noauth(self):
        self.fail()

    def test_sensor_id(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", "/monitor/status/1")
        print(rv.get_json())
        self.fail()

    def test_sensor_id_noauth(self):
        self.fail()

    def test_log(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", "/monitor/log")
        print(rv.get_json())
        self.fail()

    def test_log_noauth(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
