import unittest
from singleton import SingletonMeta
from webserver import MyServer

class TestSingleton(unittest.TestCase):

    def test_singleton(self):
        instance1 = MyServer()
        instance2 = MyServer()
        self.assertIs(instance1, instance2)

if __name__ == '__main__':
    unittest.main()
