import unittest
from webserver import MyServer

class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        instance1 = MyServer('localhost', 8080)  # Pass required arguments
        instance2 = MyServer('localhost', 8080)  # Pass required arguments
        self.assertIs(instance1, instance2)

if __name__ == "__main__":
    unittest.main()
