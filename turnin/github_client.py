import os
import json
from urllib.request import Request, urlopen
from urllib.error import URLError

from turnin.client import Client
from turnin.config import ConfigurationManager


class GithubClient(Client):

    root_url = "https://api.github.com"
    root_domain = "https://github.com"

    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.headers = {
            "Authorization": f"Bearer {self.config.access_token}",
            "Accept": "application/vnd.github.v3+json",
        }

    @staticmethod
    def authenticate() -> str:
        """Invokes oath flow and Passes authentication to configuration manager"""
        access_token = os.getenv("GITHUB_ACCESS_TOKEN")
        return access_token

    def verify_access_token(self):
        """Sends an API call to verify programme was given appropriate rights"""
        try:
            # fetch user details (every resource is identity scoped)
            headers = {
                "Accept": "application/vnd.github.v3+json", 
                "Authorization": "Bearer " + self.config.access_token
            }
            request = Request("https://api.github.com/user", headers=headers)
            response = json.loads(urlopen(request).read().decode())
            
            if response["email"] is None:
                raise RuntimeError("Could not extract email using github access token.")        
            if response["email"] != self.student_email:
                raise RuntimeError(f"Provided email ({self.student_email}) in configuration does not match Github account ({response['email']})")
        except AssertionError as e:
            raise RuntimeError(f"Access token not defined, did you run python -m turnin init? Error: {e}")
        except URLError as e:
            raise RuntimeError(f"Access token not valid, recieved error from github API; {e}")
        return self
    
    def fork(self, repository_url: str) -> str:
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

    def repository_api_url(self, repository_name, repository_owner) -> str:
        """Helper method for formatting repository api endpoint"""
        return os.path.join(self.root_url, "repos", repository_owner, repository_name)

if __name__ == "__main__":
    pass
