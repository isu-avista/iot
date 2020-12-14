import unittest
from tests.api.base_api_test import BaseApiTest


class ConfigTest(BaseApiTest):

    def test_read_dbconfig(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", "/api/config/dbdata")
        print(rv.get_json())
        self.fail()

    def test_read_dbconfig_noauth(self):
        self.fail()

    def test_update_dbconfig(self):
        json = dict()
        rv = BaseApiTest.auth_put(self.client, "admin", "admin", route="/api/config/dbdata", json=json)
        print(rv.get_json())
        self.fail()

    def test_update_dbconfig_noauth(self):
        self.fail()

    def test_update_dbconfig_nojson(self):
        self.fail()

    def test_read_sysconfig(self):
        rv = BaseApiTest.auth_get(self.client, "admin", "admin", "/api/config/sysdata")
        print(rv.get_json())
        self.fail()

    def test_read_sysconfig_noauth(self):
        self.fail()

    def test_update_sysconfig(self):
        json = dict()
        rv = BaseApiTest.auth_put(self.client, "admin", "admin", route="/api/config/sysdata", json=json)
        print(rv.get_json())
        self.fail()

    def test_update_sysconfig_noauth(self):
        self.fail()

    def test_update_sysconfig_nojson(self):
        self.fail()

    def test_read_unknown_section(self):
        self.fail()

    def test_update_unknown_section(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
