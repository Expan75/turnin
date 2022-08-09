"""Deletegates calls to OS ssh tool"""
import os
import subprocess


def generate_keypair(email: str, algorithm="ed25519") -> str:
    private_keypath = os.path.join(
        os.path.expanduser("~"), 
        f".ssh/id_{algorithm}_turnin"
    )
    public_keypath = private_keypath + ".pub"
    if os.path.exists(private_keypath):
        print(f"key already exists, reusing {public_keypath}")
    else:
        args = [
            "ssh-keygen",
            "-t",
            "rsa",
            "-f",
            private_keypath,
            "-C",
            email
        ]
        result = subprocess.run(args, encoding="utf-8", capture_output=True)
        if "Your identification has been saved".lower() not in result.stdout.lower():
            raise RuntimeError(f"something went wrong when creating ssh key: {result.stderr}")

    if not identity_is_added_to_agent(email):
        user_input = input(
            """Key is not yet added ssh-agent. 
            This will require you to write your passphrase each
            time you use git. Would you like to add the key to the agent
            to avoid having to write in your passphrase each time? [y/n]:
            """
        )
        if user_input.lower().split() == "y":
            print("adding key to agent...")
            add_key_to_agent(private_keypath)
        else:
            print("skipping adding key to agent...")

    with open(public_keypath, "r") as public_key:
        return public_key.read()


def identity_is_added_to_agent(email: str) -> bool:
    args = [
        "ssh-add",
        "-L"
    ]
    result = subprocess.run(args, encoding="utf-8", capture_output=True)
    return email.lower() in result.stdout.lower()


def add_key_to_agent(private_keypath: str):
    args = [
        "ssh-add",
        private_keypath
    ]
    result = subprocess.run(args, encoding="utf-8", capture_output=True)
    if "identity added" in result.stdout.lower():
        print("Successfully added key to agent!")
    else:
        print("Error: %s" % result.stderr)
        print("Make sure your SSH agent is up and running!")
        raise RuntimeError("Could not add key to ssh agent")