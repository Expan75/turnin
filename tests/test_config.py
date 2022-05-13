import unittest
from src.turnin import config


class TestConfig(unittest.TestCase):
    
    def test_module_exists(self):
        self.assertIsNotNone(config)

if __name__ == "__main__":
    unittest.main()
