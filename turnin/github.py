import os
from dataclasses import dataclass

from turnin import requests
from turnin.provider import BackendProviderClient


GITHUB_CLIENT_APP_ID = "Iv1.8e52222238324e4d"


@dataclass
class OathDeviceCodeResponse:
    device_code: str
    user_code: str
    verification_uri: str
    expires_in: int
    interval: int


class GithubClient(BackendProviderClient):

    root_url = "https://api.github.com"

    def __init__(self, access_token: str):
        self.access_token = access_token

    @staticmethod
    def authenticate() -> str:
        """Initiates oath device flow for Github authentication. 
            Returns an oath token that can be used to authenticate future responses.
        """
        device_code_data = GithubClient.request_oath_device_code()
        user_input = GithubClient.prompt_oath_user_action(device_code_data)
        
        if "exit" in user_input:
            exit(2)
        
        access_token = GithubClient.request_oath_access_token(device_code_data)
        
        return access_token
        
    @staticmethod
    def request_oath_device_code() -> OathDeviceCodeResponse:
        """Invokes the github device oath flow, grabbing a oath object that the user can ack"""
        response = requests.post("https://github.com/login/device/code", data={
            "client_id": GITHUB_CLIENT_APP_ID
        })        
        return OathDeviceCodeResponse(**response)
    
    @staticmethod
    def prompt_oath_user_action(oath_device_data: OathDeviceCodeResponse) -> str:
        """Stalls until user has verified that they've put in their access code on github"""
        user_input = None
        while user_input not in set("", "exit"):
            user_input = input("""
                Please proceed to {verification_uri} and enter the code: {user_code} to complete authentication.
                Once you have authenticated, you can proceed by hitting enter! Type "exit" to exit.
            """)
        return user_input

    @staticmethod
    def request_oath_access_token(oath_device_data: OathDeviceCodeResponse) -> str:
        """Assuming user has greenlit oath flow via github.com, extracts access_token"""
        response = requests.post("https://github.com/login/oauth_access", data={
            "client_id": oath_device_data.client_id,
            "device_code": oath_device_data.device_code,
            # https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
        })
        access_token = response.get("access_token")
        if not access_token:
            raise RuntimeError("no access token could be found at the end of oauth flow")
        return access_token

    def fork(self, repository_url: str):
        """Forks a repository given valid access token"""
        # In accordance /w https://docs.github.com/en/rest/repos/forks#create-a-fork
        owner_name, repository_name = repository_url.replace('.git', "").split("/")[-2:]
        url = os.path.join(self.root_url, "repos", owner_name, repository_name, "forks")
        headers = {
            "Accept": "application/vnd.github.v3+json", 
            "Authorization": "Bearer " + self.access_token
        }
        forked_repository_url = requests.post(url, headers=headers).get('html_url')
        print("Forked in progress, should be viewable on %s" % forked_repository_url)
        return forked_repository_url

    def invite_collaborator(self, repository_name: str, collaborator_email: str):
        raise NotImplementedError

    def create_pull_request(self, assignment_name: str):
        raise NotImplementedError

        
if __name__ == "__main__":
    pass