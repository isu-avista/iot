import unittest
from tests.api.base_api_test import BaseApiTest


class ServerTest(BaseApiTest):

    def test_create_server(self):
        json = dict()
        rv = BaseApiTest.auth_post(self.client, "admin", "admin", route="/api/servers", json=json)
        print(rv.get_json())
        self.fail()

    def test_read_servers(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", route="/api/servers")
        print(rv.get_json())
        self.fail()

    def test_update_server(self):
        json = dict()
        rv = BaseApiTest.auth_put(self.client, "admin", "admin", route="/api/servers/1", json=json)
        print(rv.get_json())
        self.fail()

    def test_delete_server(self):
        rv = BaseApiTest.auth_delete(self.client, "admin", "admin", route="/api/servers/1")
        print(rv.get_json())
        self.fail()


if __name__ == '__main__':
    unittest.main()
