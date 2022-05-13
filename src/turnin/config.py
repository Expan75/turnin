"""Actions for managing tool configuration and setup"""
import os
import json
from typing import List
from dataclasses import dataclass

from turnin import BRAND

CONFIGURATION_FILEPATH = os.path.join(os.path.expanduser("~"), f".{BRAND}")

@dataclass
class Configuration():
    student_email: str
    github_access_token: str
    instructor_email_addresses: List[str]

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
            instructor_email = input('Please input the email of your instructor: ')
            instructor_emails.append(instructor_email)
            add_more_toggle = True if input("Would you like to add another? 1. Yes, 2. No") == 1 else False
        github_access_token = input('Please input your github access token: ')

        # TODO: currently there's no validation. Probably we'd restart the entire flow for simplicty.
        print("initialising and writing configuration...")
        configuration = Configuration(
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
            raise FileNotFoundError("ERROR: no config file found. Did you forget to call run init? -> python3 -m turnin init")
        parsed_configuration = json.loads(configuration)
        return Configuration(**parsed_configuration)

    def write(self):
        with open(CONFIGURATION_FILEPATH, 'w+') as f:
            json.dump({
                'student_email': self.student_email,
                'github_access_token': self.github_access_token,
                'instructor_email_addresses': self.instructor_email_addresses    
            }, f)
        return self


if __name__ == '__main__':
    config = Configuration.init()
    print("initalised conf as: ", config)
    config.student_email = "stefan@google.com"
    config.write()
    print("update and ensure it's different...")
    del config
    config = Configuration.read()
    print("updated conf: ", config)