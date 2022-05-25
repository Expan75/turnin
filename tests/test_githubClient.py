import unittest
from unittest.mock import patch

from turnin.github_client import GithubClient

class TestGithubClient(unittest.TestCase):

    def test_class_exists(self):
        self.assertIsNotNone(GithubClient)


if __name__ == "__main__":
    unittest.main()