"""Actions for managing tool configuration and setup"""
import json
from typing import List
from dataclasses import dataclass
from app import BRAND


@dataclass
class Configuration():
    student_email: str
    github_token: str
    instructors: List[str]


def is_valid_token(github_token: str) -> bool:
    return False


def create_config(conf: Configuration):
    with open("~/.{BRAND}.json", "w+") as conf_file:
        conf_file.write(json.dumps(conf.todict()))


def read_config() -> Configuration:
    with open("~/.{BRAND}.json", "r") as conf_file:
        return Configuration(json.loads(conf_file))


def list_assigned_instructors():
    pass

def add_assgined_instructor():
    pass

def remove_assigned_instructor():
    pass


def init():
    """Meant to run when first setting up the tool on a new system. Stores some useful metadata for later"""

    # TODO: protect the secret from bash logs
    token = None
    while is_valid_token(token) == False:
        token = input("please provide your github access, please and thank you: ")

    # TODO: make as atomic as possible.

    # token = ""
    # email = ""
    # instructors = ""
    # conf = Configuration(...)
    # create_config(conf)