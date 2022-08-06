import os
import json
import logging
from typing import List, Optional
from dataclasses import dataclass, asdict
from pprint import pprint

log = logging.getLogger(__name__)


TURNIN_DIRECTORY = os.path.join(os.path.expanduser("~"), ".turnin")
TURNIN_CONFIGURATION_FILE = os.path.join(TURNIN_DIRECTORY, "config.json")


@dataclass
class Configuration:
    provider: str
    user_email: str
    instructor_email_addresses: List[str]
    ssh_key_path: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None

    @classmethod
    def initialize(cls):
        """Set up configuration object if nothing exists"""
        if os.path.exists(TURNIN_CONFIGURATION_FILE):
            print(f"Detected existing configuration at {TURNIN_CONFIGURATION_FILE}")
            prompt_response = input(
                "Do you want to overwrite exinsting configuration? y/n: "
            )
            if prompt_response.strip().lower() != "y":
                return cls.read()
            else:
                print(f"Removing {TURNIN_CONFIGURATION_FILE}.")
                os.remove(TURNIN_CONFIGURATION_FILE)

        config_data = {
            "provider": cls.prompt_provider(),
            "user_email": cls.prompt_email(),
            "instructor_email_addresses": cls.prompt_instructors(),
        }
        log.debug(f"writing init to file: {config_data=}")
        return Configuration(**config_data).write()

    @classmethod
    def prompt_provider(cls, provider=None) -> str:
        providers = {1: "GitHub"}
        pprint(providers, indent=4)
        provider_key = input(f"Please one of the above providers by number: ")
        if (provider := providers.get(int(provider_key))) is None:
            return cls.prompt_provider()
        print(f"Provider selected as {provider}!")
        return provider

    @classmethod
    def prompt_email(cls, email=None, confirmed_email=None) -> str:
        if email is not None and email == confirmed_email:
            return email
        elif email is not None and confirmed_email is not None:
            print(f"{email=} mismatch against {confirmed_email=}")
        email = input("Please enter your email address: ")
        confirmed_email = input("Please enter your confirmed email address: ")
        return cls.prompt_email(email, confirmed_email)

    @classmethod
    def prompt_instructors(cls, instructors=[]) -> List[str]:
        instructors.append(input("Please enter the email of your instructor: "))
        add_another = input("Would you like to add another? [y/n]: ")
        if add_another == "y":
            return cls.prompt_instructors(instructors)
        return instructors

    def write(self):
        os.makedirs(TURNIN_DIRECTORY, exist_ok=True)
        with open(TURNIN_CONFIGURATION_FILE, "w") as f:
            json.dump(asdict(self), f, indent=4)
        return self

    @staticmethod
    def read():
        with open(TURNIN_CONFIGURATION_FILE, "r") as f:
            return Configuration(**json.load(f))

    @classmethod
    def verify(cls):
        config = cls.read()

    def update_email(self, email: str):
        pass

    def add_instructor(self, instructor: str):
        pass

    def remove_instructor(self, instructor: str):
        pass


if __name__ == "__main__":
    Configuration.initialize()
