import os
import json
from urllib.request import Request, urlopen

from turnin.config import ConfigurationManager
from turnin.provider import BackendProviderClient


class GithubClient(BackendProviderClient):

    root_url = "https://api.github.com"
    root_domain = "https://github.com"

    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.headers = {
            "Authorization": f"Bearer {self.config.github_access_token}",
            "Accept": "application/vnd.github.v3+json",
        }
    
    def fork(self, repository_url: str):
        """Forks a repository given valid access token""" 
        # In accordance /w https://docs.github.com/en/rest/repos/forks#create-a-fork
        owner_name, repository_name = repository_url.replace('.git', "").split("/")[-2:] 
        url = os.path.join(self.root_url, "repos", owner_name, repository_name, "forks")
        with urlopen(Request(url, method="POST", headers=self.headers)) as response:
            forked_repository_url = json.loads(response.read().decode())["html_url"]
            print("Forked in progress, should be viewable on %s" % forked_repository_url)
            return forked_repository_url

    def invite_collaborator(self, repository_name: str, collaborator_email: str):
        raise NotImplementedError

    def create_pull_request(self, assignment_name: str):
        raise NotImplementedError


if __name__ == "__main__":
    pass