import unittest
from unittest.mock import patch

from turnin.config import ConfigurationManager
from turnin.github_client import GithubClient

class TestGithubClient(unittest.TestCase):

    config = ConfigurationManager.read()
    client = GithubClient(config)

    def test_class_exists(self):
        self.assertIsNotNone(self.client)

    @patch('builtins.print', lambda x: x) 
    def test_fork(self):
        sample_repo_url = "https://github.com/octocat/Hello-World" 
        """NOTE: we don't have delete rights on the token so manual cleanup is required here"""
        respository_url_1 = self.client.fork(sample_repo_url)
        respository_url_2 = self.client.fork(sample_repo_url)
        self.assertIsNotNone(respository_url_1)
        self.assertIsNotNone(respository_url_1)
        self.assertTrue(respository_url_1 == respository_url_2)
    
    def test_invite_collaborator(self):
        pass

    def test_create_pull_request(self):
        pass


if __name__ == "__main__":
    unittest.main()