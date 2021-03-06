import fire

from turnin import git
from turnin.github_client import GithubClient
from turnin.config import ConfigurationManager

VERSION = "0.0.1"


class AssignmentCommands:
    """Use this subcommand to submit homework assignments"""

    def create(self, template_url: str, pathname: str = None):
        git.clone(template_url, pathname)

    def submit(self):
        pass

        # NOTE: all of the below steps should be encased in some sort of progressbar

        # find folder and validate it is a valid submission
        # cd to the shadow repo and make a new submission
        # copy the entire submission folder to the local shadow repo
        # git+add+commit+push the added folder and contained files
        # verify success

class Commands:
    """CLI tools for automating homework template usage and submissions"""    
    def __init__(self):
        self.homework = AssignmentCommands()
    
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
