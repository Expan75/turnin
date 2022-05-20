import fire

from config import Configuration


VERSION = "0.0.1"


class AssignmentCommands:
    """Use this subcommand to submit homework assignments"""

    def create(self):
        print("Creating assignment")

    def submit(self):
        print("Submitting assignment")


class Commands:
    """CLI tools for automating homework template usage and submissions"""    
    def __init__(self):
        self.assignment = AssignmentCommands()
    
    def init(self):
        """Initalises the tool and sets up configuration."""
        Configuration.init()

    def verify(self):
        """Verifies the integrity of the tool and its initalisation."""
        Configuration.verify()
        print("Initalisation successful. Ready to go!")

    
    def version(self):
        """Returns the version of the tool."""
        print(f"turnin-cli v{VERSION}")


if __name__ == "__main__":
    fire.Fire(Commands)
