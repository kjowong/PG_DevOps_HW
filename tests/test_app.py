from app import request_app
import unittest
import requests


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = request_app.app.test_client()

    def test_get_no_header(self):
        url = "http://0.0.0.0:5000/"
        headers = None
        response = self.app.get(url, headers=headers)
        self.assertEqual(response.data, '<p>Hello, World</p>')

    def test_get_correct_header(self):
        url = "http://0.0.0.0:5000/"
        headers = {"Accept": "application/json"}
        response = self.app.get(url, headers=headers)
        self.assertEqual(response.data, '{"message": "Good morning"}')

    def test_post(self):
        url = "http://0.0.0.0:5000/"
        response = self.app.post(url)
        self.assertEqual(response.data, "This is a POST request")

    def tearDown(self):
        self.app.delete()


if __name__ == "__main__":
    unittest.main()
