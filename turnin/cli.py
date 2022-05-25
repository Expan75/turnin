import fire

from config import ConfigurationManager
from github_client import GithubClient

VERSION = "0.0.1"


class AssignmentCommands:
    """Use this subcommand to submit homework assignments"""

    def create(self, template_url: str):
        print(f"Creating assignment based on template: {template_url}")
        if "github" in template_url:
            config = ConfigurationManager.read()
            github_client = GithubClient(config)
        else:
            raise NotImplementedError(f'Not valid domain ({template_url.split("")[:1]}) to source templates from.')


    def submit(self):
        print("Submitting assignment")


class Commands:
    """CLI tools for automating homework template usage and submissions"""    
    def __init__(self):
        self.assignment = AssignmentCommands()
    
    def init(self):
        """Initalises the tool and sets up configuration."""
        ConfigurationManager.init()

    def verify(self):
        """Verifies the integrity of the tool and its initalisation."""
        ConfigurationManager.verify()
        print("Initalisation successful. Ready to go!")

    
    def version(self):
        """Returns the version of the tool."""
        print(f"turnin-cli v{VERSION}")


if __name__ == "__main__":
    fire.Fire(Commands)
