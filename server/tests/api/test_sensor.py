import unittest
from tests.api.base_api_test import BaseApiTest


class SensorTest(BaseApiTest):

    def test_create_sensor(self):
        json = dict()
        rv = BaseApiTest.auth_post(self.client, "admin", "admin", route="/api/sensors", json=json)
        print(rv.get_json())
        self.fail()

    def test_read_sensors(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", route="/api/sensors")
        print(rv.get_json())
        self.fail()

    def test_update_sensor(self):
        json = dict()
        rv = BaseApiTest.auth_put(self.client, "admin", "admin", route="/api/sensors/1", json=json)
        print(rv.get_json())
        self.fail()

    def delete_sensor(self):
        rv = BaseApiTest.auth_delete(self.client, "admin", "admin", route="/api/sensors/1")
        print(rv.get_json())
        self.fail()


if __name__ == '__main__':
    unittest.main()
