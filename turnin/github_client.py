import os

from turnin.git_provider_client import GitProviderClient
from turnin.config import ConfigurationManager


class GithubClient(GitProviderClient):

    def __init__(self, config: ConfigurationManager):
        self.config = config
    
    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.config.github_access_token}",
            "Accept": "application/json",
        }

    def clone(self, repository_url: str):
        """Clone a github repository via system git tool"""
        raise NotImplementedError 

    def create_pull_request(self, assignment_name: str):
        raise NotImplementedError

    def download_repository(self, repository_url: str, local_path: str = "."):
        """Fetches a full or partial repository but removes .git and .gitignore files"""
        cloneable_url = self.get_cloneable_url(repository_url)
        print("cloneable_url: ", cloneable_url)
   
    def fork(self, repository_url: str, new_repository_name: str):
        """Forks a repository given valid access token"""
        raise NotImplementedError
    
    def invite_collaborator(self, repository_name: str, collaborator_email: str):
        raise NotImplementedError

    @staticmethod
    def get_cloneable_url(repository_url: str):
        #TODO: needs to be way more robust.
        return "https://" + os.path.join(*repository_url.split("/")[:3])


if __name__ == "__main__":
    config = ConfigurationManager.read()
    client = GithubClient(config)