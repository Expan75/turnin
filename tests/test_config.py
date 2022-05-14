import unittest
from unittest.mock import patch
from turnin import config


class TestConfig(unittest.TestCase):
    
    def test_module_exists(self):
        self.assertIsNotNone(config)

    def test_class_exists(self):
        self.assertIsNotNone(config.Configuration)

    """
    @patch('config.CONFIGURATION_FILEPATH', '/tmp/somefile.json')
    def test_read_non_existing_config(self):
        with self.assertRaises(FileNotFoundError):
            config.Configuration.read()
    """

if __name__ == "__main__":
    unittest.main()
