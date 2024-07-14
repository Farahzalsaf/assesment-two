import unittest
import asyncio
from iterators import RequestIterator, async_request_handler, AsyncRequestIterator

class TestIterators(unittest.TestCase):

    def test_request_iterator(self):
        requests = ['request1', 'request2', 'request3']
        iterator = RequestIterator(requests)
        result = list(iterator)
        self.assertEqual(result, requests)

    def test_async_request_handler(self):
        requests = ['request1', 'request2', 'request3']
        asyncio.run(async_request_handler(requests))

if __name__ == '__main__':
    unittest.main()