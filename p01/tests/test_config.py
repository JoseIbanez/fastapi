import unittest
from cifastapi.config import safeget,getConfig,getVersion

class ConfigTest(unittest.TestCase):

    def test_version(self):
        version = getVersion()
        self.assertTrue(version)

    def test_config_01(self):
        value = getConfig("user.1")
        self.assertTrue(value)

    def test_safeget(self):
        ret = safeget({"a":1},"a")
        self.assertEqual(ret,1)

if __name__ == '__main__':
    unittest.main()
