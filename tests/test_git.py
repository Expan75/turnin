import unittest
from unittest.mock import patch

from turnin import git


class TestGithubClient(unittest.TestCase):

    def test_module_exists(self):
        self.assertIsNotNone(git)

    def test_class_exists(self):
        self.assertIsNotNone(git.GitHubClient)


if __name__ == "__main__":
    unittest.main()