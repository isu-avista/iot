import unittest
from tests.api.base_api_test import BaseApiTest
import os


class ServiceTest(BaseApiTest):

    def test_ping(self):
        rv = self.client.get('/ping')
        self.assertIn('pong!', rv.get_json())


if __name__ == '__main__':
    unittest.main()
