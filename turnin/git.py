"""Module for complete git workflow, extendable for different providers (github only as of now)."""
import os
import typing as t
from abc import ABC, abstractmethod


class GitProviderClient(ABC):

    @abstractmethod
    def fork(self, repository_url: str, new_repository_name: str):
        pass

    @abstractmethod
    def create_pull_request(assignment_name: str):
        pass

    @abstractmethod
    def invite_collaborator(collaborator_email: str):
        pass

    @abstractmethod
    def download_repository(repo_url: str, local_path: str):
        pass
    

class GithubClient(GitProviderClient):

    def __init__(self, github_access_token: str, ssh_key: str):
        self.access_token = github_access_token
        self.ssh_key = ssh_key

    def fork(self, repository_url: str, new_repository_name: str):
        raise NotImplementedError

    def create_pull_request(self, assignment_name: str):
        raise NotImplementedError
    
    def download_repository(self, repository_url: str, local_path: str = None):
        raise NotImplementedError

    def invite_collaborator(self, repository_name: str, collaborator_email: str):
        raise NotImplementedError

if __name__ == "__main__":
    github_client = GithubClient(os.getenv("GITHUB_ACCESS_TOKEN"))
    