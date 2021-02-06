import unittest
from cifastapi.config import safeget

class Dummy(unittest.TestCase):

    def test_dummy_01(self):
        self.assertGreater(2, 1)

    def test_dummy_02(self):
        self.assertGreater(2, 1)

    def test_safeget(self):
        ret = safeget({"a":1},"a")
        self.assertEqual(ret,1)

if __name__ == '__main__':
    unittest.main()
