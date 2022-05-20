"""Actions for managing tool configuration and setup"""
import os
import json
import urllib.request
import urllib.error
import subprocess
from typing import List
from dataclasses import dataclass

CONFIGURATION_FILEPATH = os.path.join(os.path.expanduser("~"), ".turnin")

@dataclass
class ConfigurationManager:
    student_email: str
    github_access_token: str
    instructor_email_addresses: List[str]

    @staticmethod
    def init():
        """Starts the inital flow to create a configuration file"""

        if os.path.isfile(CONFIGURATION_FILEPATH):
            print("Configuration file already exists. Are you sure you would like to override it?")
            if "reinit" != input("To override and reinitalise, enter 'reinit': "):
                print("exiting...")
                exit(2)
            else:
                print("proceeding with reinit...")

        student_email = input('Please input your email: ')
        instructor_emails = []
        add_more_toggle = True
        while len(instructor_emails) < 1 or add_more_toggle:
            instructor_email = input('Please input the email of an assigned instructor: ')
            instructor_emails.append(instructor_email)
            add_more_toggle = True if input("Would you like to add another? (y/n): ") == "y" else False
        github_access_token = input('Please input your github access token: ')

        # TODO: currently there's no validation. Probably we'd restart the entire flow for simplicty.
        print("initialising and writing configuration...")
        configuration = ConfigurationManager(
            student_email=student_email, 
            instructor_email_addresses=instructor_emails,
            github_access_token=github_access_token
        ).write()
        print(f"successfully wrote configuration to disk")
        return configuration

    @staticmethod
    def read():
        try:
            with open(CONFIGURATION_FILEPATH, 'r') as f:
                configuration = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                "ERROR: no config file found. Did you forget to call run init? -> python3 -m turnin init"
            )
        parsed_configuration = json.loads(configuration)
        return ConfigurationManager(**parsed_configuration)

    def write(self):
        with open(CONFIGURATION_FILEPATH, 'w+') as f:
            json.dump({
                'student_email': self.student_email,
                'github_access_token': self.github_access_token,
                'instructor_email_addresses': self.instructor_email_addresses    
            }, f, indent=4)
        return self

    @staticmethod
    def verify():
        """Utility method for ensuring installation and configuration integrity"""
        try:
            config = ConfigurationManager.read().verify_ssh_to_github().verify_accesss_token_to_github()
            print("SUCCESS: verification was successful. You should now be able to submit assignments!")
            return config      
        except (NotImplementedError, FileNotFoundError, RuntimeError) as e:
            raise e

    def verify_ssh_to_github(self):
        ssh_to_github_process = subprocess.run(["ssh","-T", "git@github.com"], encoding="utf-8", capture_output=True)
        if (
            ("You've successfully authenticated" not in ssh_to_github_process.stdout)
            and ("You've successfully authenticated" not in ssh_to_github_process.stderr)
        ):
            raise RuntimeError(f"Authenticated ssh connection to Github could not be established. Output {ssh_to_github_process.stderr}")
        return self

    def verify_accesss_token_to_github(self):
        try:
            # fetch user details (every resource is identity scoped)
            headers={
                "Accept": "application/vnd.github.v3+json", 
                "Authorization": "Bearer " + self.github_access_token
            }
            request = urllib.request.Request("https://api.github.com/user", headers=headers)
            response = json.loads(urllib.request.urlopen(request).read().decode())
            
            if response["email"] is None:
                raise RuntimeError("Could not extract email using github access token.")        
            if response["email"] != self.student_email:
                raise RuntimeError(f"Provided email ({self.student_email}) in configuration does not match Github account ({response['email']})")
        
        except AssertionError as e:
            raise RuntimeError(f"Access token not defined, did you run python -m turnin init? Error: {e}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"Access token not valid, recieved error from github API; {e}")
        return self


if __name__ == "__main__":
    pass