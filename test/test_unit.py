import unittest
import requests
from app_service import AppService

class AppUnitTest(unittest.TestCase):
    def test_existing_user(self):
        service = AppService('users.json')
        self.assertEqual('Simon', service.get_user(1))


if __name__ == '__main__':
    unittest.main()
