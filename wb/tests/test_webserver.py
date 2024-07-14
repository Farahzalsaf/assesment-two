import unittest
from singleton import SingletonClass

class TestWebServer(unittest.TestCase):
    def test_singleton_instance(self):
        server1 = SingletonClass("127.0.0.1", 8081)
        server2 = SingletonClass("127.0.0.1", 8081)
        self.assertIs(server1, server2)

if __name__ == "__main__":
    unittest.main()
