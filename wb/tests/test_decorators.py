import sys
import os
import unittest

# Add the project directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from decorators import log_request, authorize_request

class TestDecorators(unittest.TestCase):
    async def dummy_func(self, request):
        return request

    def test_log_request_decorator(self):
        decorated_func = log_request(self.dummy_func)
        self.assertIsNotNone(decorated_func)

    def test_authorize_request_decorator(self):
        decorated_func = authorize_request(self.dummy_func)
        self.assertIsNotNone(decorated_func)

if __name__ == "__main__":
    unittest.main()