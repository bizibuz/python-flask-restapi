import unittest
import requests

class AppIntegrationTest(unittest.TestCase):
    def test_existing_user(self):
        res = requests.get('http://localhost:5000/1')
        self.assertTrue(res.text == 'Hello, Simon!' or res.text == 'Hello Tai Man!')

    def test_invalid_user(self):
        res = requests.get('http://localhost:5000/10')
        self.assertEqual('Hello, World!', res.text)

if __name__ == '__main__':
    unittest.main()
