import unittest
from generators import response_generator, streaming_response_generator

class MockHandler:
    def __init__(self):
        self.response = []

    def send_response(self, code):
        self.response.append(f"Response code: {code}")

    def send_header(self, key, value):
        self.response.append(f"Header: {key}={value}")

    def end_headers(self):
        self.response.append("End headers")

    def wfile_write(self, data):
        self.response.append(f"Body: {data}")

class TestGenerators(unittest.TestCase):

    def test_response_generator(self):
        handler = MockHandler()
        gen = response_generator(handler, "Test content")
        result = list(gen)
        self.assertIn(b"Test content", result)

    def test_streaming_response_generator(self):
        handler = MockHandler()
        gen = streaming_response_generator(handler)
        result = list(gen)
        self.assertTrue(all([b"Stream chunk" in chunk for chunk in result]))

if __name__ == '__main__':
    unittest.main()