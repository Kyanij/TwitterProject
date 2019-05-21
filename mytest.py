import unittest

def hello():
    return 'hello'

class TestString(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(hello(), 'hello')

if __name__ == '__main__':
    unittest.main()


