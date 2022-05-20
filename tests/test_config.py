import os
import tempfile
import unittest
from unittest.mock import patch

from turnin import config


class TestConfig(unittest.TestCase):

    configuration_filepath = os.path.join(tempfile.gettempdir(), '.turnin.json')

    def test_module_exists(self):
        self.assertIsNotNone(config)

    def test_class_exists(self):
        self.assertIsNotNone(config.ConfigurationManager)
    
    def test_read_non_existing_config(self):
        config.CONFIGURATION_FILEPATH = self.configuration_filepath
        with self.assertRaises(FileNotFoundError):
            config.ConfigurationManager.read()

    def test_config_write(self):
        with tempfile.TemporaryDirectory() as _dir:
            config.CONFIGURATION_FILEPATH = os.path.join(_dir, '.turnin.json')
            persisted_configuration = config.ConfigurationManager('', '', ['']).write()
            self.assertIsNotNone(persisted_configuration)
            self.assertIsNotNone(config.ConfigurationManager.read())
            self.assertEqual(persisted_configuration, config.ConfigurationManager.read())

    def test_github_access_verification(self):
        with tempfile.TemporaryDirectory() as _dir:
            config.ConfigurationManager.verify_accesss_token_to_github.response = { "email": "test@test.com" } 
            config.CONFIGURATION_FILEPATH = os.path.join(_dir, '.turnin.json')
            with self.assertRaises(RuntimeError):
                # should yield 401 as no valid access token is provided.
                config.ConfigurationManager('test@test.com', '', ['']).write().verify_accesss_token_to_github()

if __name__ == "__main__":
    unittest.main()
