import fire

from config import Configuration
from constants import VERSION


class SubCommands:
    """Subcommands related to homework CRUD"""
    def ping(self):
        print("pong!")


class Commands:
    """CLI tools for automating homework template usage and submissions"""    
    def __init__(self):
        self.submodule = SubCommands()
    
    def init(self):
        """Initalises the tool, sets up github access etc., generates static file"""
        Configuration.init()

    def verify(self):
        """Verifies the integrity of the tool and its initalisation."""
        print("verifying...")
        print("Done!")
    
    def version(self):
        """Returns the version of the tool."""
        print(f"turnin-cli v{VERSION}")


if __name__ == "__main__":
    fire.Fire(Commands)