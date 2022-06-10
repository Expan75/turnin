from abc import ABC, abstractmethod


class Client(ABC):
    """Allow us to potentially which out Github to some other backend provider"""

    @abstractmethod
    def authenticate(self) -> str:
        """Can be any authentication strategy but machine oath is preferred."""
        pass

    @abstractmethod
    def fork(self, repository_url: str, new_repository_name: str):
        """Platform specific copy of a remote repository to a users own account"""
        pass
 
    @abstractmethod
    def invite_collaborator(collaborator_email: str):
        """Invite outside users to view and edit a remote repository"""
        pass

    @abstractmethod
    def create_pull_request(assignment_name: str):
        """What it sounds like"""
        pass


if __name__ == "__main__":
    pass
    
