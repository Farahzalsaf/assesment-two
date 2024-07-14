import sys
import os
import unittest

# Add the project directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from iterators import RequestIterator

class TestRequestIterator(unittest.TestCase):
    def test_iterator(self):
        requests = ["req1", "req2", "req3"]
        iterator = RequestIterator(requests)
        result = [req for req in iterator]
        self.assertEqual(result, requests)

if __name__ == "__main__":
    unittest.main()