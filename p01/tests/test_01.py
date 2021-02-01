import unittest

class Dummy(unittest.TestCase):

    def test_dummy_01(self):
        self.assertGreater(2, 1)

    def test_dummy_02(self):
        self.assertGreater(2, 1)


if __name__ == '__main__':
    unittest.main()
