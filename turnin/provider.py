from abc import ABC, abstractmethod


class BackendProviderClient(ABC):
    """Allow us to potentially which out Github to some other backend provider"""

    @abstractmethod
    def authenticate():
        pass 

    @abstractmethod
    def fork(repository_url: str, new_repository_name: str):
        pass
 
    @abstractmethod
    def invite_collaborator(collaborator_email: str):
        pass

    @abstractmethod
    def create_pull_request(assignment_name: str):
        pass


if __name__ == "__main__":
    pass
    