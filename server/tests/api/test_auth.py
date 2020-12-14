import unittest
from tests.api.base_api_test import BaseApiTest
from flask import jsonify


class AuthTest(BaseApiTest):

    def test_login(self):
        json = dict(
            email="admin",
            password="admin"
        )
        rv = self.client.post('/api/login', json=json)
        self.fail()

    def test_login_bad_user(self):
        self.fail()

    def test_login_bad_password(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
