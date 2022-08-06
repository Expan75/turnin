import os
import json
import requests
import subprocess
from typing import Tuple
from turnin.provider import Provider
from turnin.config import Configuration
from dataclasses import dataclass


@dataclass
class OauthChallengeResponse:
    device_code: str
    user_code: str
    verification_uri: str
    expires_in: int
    interval: int


@dataclass
class DeviceAccessTokenResponse:
    access_token: str
    expires_in: int
    refresh_token: str
    refresh_token_expires_in: int
    token_type: str
    scope: str


class GitHub(Provider):
    def __init__(self, config: Configuration):
        self.base = "https://api.github.com"
        self.client_id = "Iv1.8e52222238324e4d"
        self.config = config

    @property
    def headers(self) -> dict[str:str]:
        headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
        }
        if self.config.access_token is not None:
            headers.update({"Authorization": "Bearer " + self.config.access_token})
        return headers

    def start_oauth_challenge(self) -> OauthChallengeResponse:
        """Fetches the challenge to be solved by a user"""
        if self.client_id is None:
            RuntimeError("No GITHUB_CLIENT_ID provided in environment.")
        endpoint = "https://github.com/login/device/code"
        response = requests.post(
            endpoint, headers=self.headers, data=json.dumps({"client_id": self.client_id})
        )
        if (response_code := response.status_code) != 200:
            raise RuntimeError(
                f"Tried to start oauth challenge but got {response_code}"
            )

        return OauthChallengeResponse(**response.json())

    def prompt_oauth_user(self, oauth_challenge: OauthChallengeResponse):
        """
        Blocks until user presses enter to signal succesfully completing
        their part of the oauth authentication flow.
        """
        input(
            f"""
                Please head over to {oauth_challenge.verification_uri} using a webbrowser 
                and input the code: {oauth_challenge.user_code}. Take your time, and press enter when you're done!
            """
        )

    def complete_oauth_challenge(
        self, oauth_challenge: OauthChallengeResponse
    ) -> DeviceAccessTokenResponse:
        endpoint = "https://github.com/login/oauth/access_token"
        response = requests.post(
            endpoint,
            headers=self.headers,
            data=json.dumps({
                "client_id": self.client_id,
                "device_code": oauth_challenge.device_code,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            }),
        )
        if (response_code := response.status_code) != 200:
            raise RuntimeError(
                f"Tried to start oauth challenge but got {response_code}"
            )
        return OauthChallengeResponse(**response.json())

    def authenticate(self) -> Tuple[str, str]:
        """Invokes oath flow and passes authentication tokens"""
        challenge = self.start_oauth_challenge()
        self.prompt_oauth_user(challenge)
        completed_challenge = self.complete_oauth_challenge(challenge)
        self.config.access_token = completed_challenge.access_token
        self.config.refresh_token = completed_challenge.refresh_token
        return self

    def verify_ssh_key(self):
        ssh_to_github_process = subprocess.run(
            ["ssh", "-T", "git@github.com"], encoding="utf-8", capture_output=True
        )
        if (
            "You've successfully authenticated" not in ssh_to_github_process.stdout
        ) and ("You've successfully authenticated" not in ssh_to_github_process.stderr):
            raise RuntimeError(
                f"Authenticated ssh connection to Github could not be established. Output {ssh_to_github_process.stderr}"
            )
        return self

    def verify_access_token(self):
        """Sends an API call to verify programme was given appropriate rights"""
        endpoint = self.base + "/user"
        response = requests.get(endpoint, headers=self.headers)
        if (
            response.status_code == 200
            and (email := response.json()["email"]) is not None
        ):
            if email != self.config.user_email:
                raise RuntimeError(
                    f"Provided email ({self.config.user_email}) in configuration does not match Github account ({response['email']})"
                )
            raise RuntimeError("Could not extract email using github access token.")

    def fork(self, repository_url: str) -> str:
        """Forks a repository given valid access token"""
        owner_name, repository_name = self.parse_repository_url(repository_url)
        endpoint = self.base + f"/repos/{owner_name}/{repository_name}/forks"
        response = requests.post(endpoint, headers=self.headers)
        if response.status_code == 200:
            forked_repository_url = response.json()["html_url"]
            print(f"Forked in progress, should be viewable on {forked_repository_url}")
        raise RuntimeError(f"Could not fork based off {repository_url=}")

    def parse_repository_url(self, url) -> Tuple[str, str]:
        owner_name, repository_name = url.replace(".git", "").split("/")[-2:]
        return owner_name, repository_name

    def invite_collaborator(self, repository_name: str, collaborator_email: str):
        raise NotImplementedError

    def create_pull_request(self, assignment_name: str):
        raise NotImplementedError


if __name__ == "__main__":
    pass
