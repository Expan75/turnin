import os
import unittest
from unittest.mock import patch

from turnin.config import ConfigurationManager
from turnin.github_client import GithubClient

class TestGithubClient(unittest.TestCase):

    config = ConfigurationManager(
        os.getenv("STUDENT_EMAIL"),
        os.getenv("GITHUB_ACCESS_TOKEN"),
        os.getenv("INSTRUCTOR_EMAIL_LIST").split(","),
    )
    client = GithubClient(config)

    def test_class_exists(self):
        self.assertIsNotNone(self.client)
   
    def test_fork(self):
        """NOTE: we don't have delete rights on the token so manual cleanup is required here"""
        self.client.fork("https://github.com/octocat/Hello-World", "hello-world")
        with self.assertRaises(RuntimeError):
            self.client.fork("https://github.com/octocat/Hello-World", "hello-world")

    def test_invite_collaborator(self):
        pass

    def test_create_pull_request(self):
        pass


if __name__ == "__main__":
    unittest.main()