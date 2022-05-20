"""Module for interacting with Github"""
from abc import ABC, abstractmethod

from turnin.config import ConfigurationManager 


class GitProviderClient(ABC):

    @abstractmethod
    def fork():
        pass

    @abstractmethod
    def add_collaborator():
        pass


class GitHubClient(GitProviderClient):

    def __init__(self, github_access_token: str):
        self.access_token = github_access_token

    def fork(self, repository_url: str, new_repository_name: str):
        raise NotImplementedError

    def add_collaborator(self, repository_name: str, collaborator_email: str):
        raise NotImplementedError