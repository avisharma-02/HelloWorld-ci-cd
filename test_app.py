import unittest
from app import hello_world

class testApp(unittest.testCase):
    def test_hello_world(self):
        self.assertequal(hello_world(),"Hello World!")

        If __name__ == '__main__':
        unittest.main()