import unittest
from inheratince import GetRequestHandler, PostRequestHandler

class MockHandler:
    def __init__(self):
        self.headers = {'Content-Length': '0'}
        self.response = []
        self.wfile = self
        self.rfile = self

    def send_response(self, code):
        self.response.append(f"Response code: {code}")

    def send_header(self, key, value):
        self.response.append(f"Header: {key}={value}")

    def end_headers(self):
        self.response.append("End headers")

    def write(self, data):
        self.response.append(f"Body: {data}")

    def read(self, length):
        return b""

class TestInheritance(unittest.TestCase):

    def test_get_request_handler(self):
        handler = MockHandler()
        get_handler = GetRequestHandler()
        get_handler.handle_request(handler)
        self.assertIn("Response code: 200", handler.response)

    def test_post_request_handler(self):
        handler = MockHandler()
        post_handler = PostRequestHandler()
        post_handler.handle_request(handler)
        self.assertIn("Response code: 200", handler.response)

if __name__ == '__main__':
    unittest.main()
