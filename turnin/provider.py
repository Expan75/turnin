from abc import ABC, abstractmethod


class Provider(ABC):
    """Allow us to potentially which out Github to some other backend provider"""

    @abstractmethod
    def authenticate(self):
        """Can be any authentication strategy but machine oath is preferred."""
        pass

    @abstractmethod
    def verify_access_ssh(self):
        """Verifies the host's ssh connection to the provider"""
        pass

    @abstractmethod
    def verify_access_token(self) -> bool:
        """Checks if a access token is valid"""
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
