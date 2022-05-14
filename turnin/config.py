"""Actions for managing tool configuration and setup"""
import os
import json
import subprocess
from typing import List
from dataclasses import dataclass

import constants

@dataclass
class Configuration():
    student_email: str
    github_access_token: str
    instructor_email_addresses: List[str]

    def init():
        """Starts the inital flow to create a configuration file"""

        if os.path.isfile(constants.CONFIGURATION_FILEPATH):
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
            with open(constants.CONFIGURATION_FILEPATH, 'r') as f:
                configuration = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                "ERROR: no config file found. Did you forget to call run init? -> python3 -m turnin init"
            )
        parsed_configuration = json.loads(configuration)
        return Configuration(**parsed_configuration)

    @staticmethod
    def verify():
        """Utility method for ensuring github connection with provided token"""
        try:
            config = Configuration.read()
            config.verify_ssh_to_github()
            config.verify_accesss_token_to_github()
        except (NotImplementedError, FileNotFoundError, RuntimeError) as e:
            raise e('ERROR: Configuration verification failed')

    def verify_ssh_to_github(self):
        process = subprocess.run(["ssh","-T", "git@github.com"], stdout=subprocess.PIPE)
        decoded_process_result = process.stdout.decode('utf-8')
        print("decoded output: ", decoded_process_result)
        if "You've successfully authenticated" not in decoded_process_result:
            raise RuntimeError(f"Authenticated ssh connection to Github could not be established. The given output was: {decoded_process_result}")

    def verify_accesss_token_to_github(self):
        raise NotImplementedError

    def write(self):
        with open(constants.CONFIGURATION_FILEPATH, 'w+') as f:
            json.dump({
                'student_email': self.student_email,
                'github_access_token': self.github_access_token,
                'instructor_email_addresses': self.instructor_email_addresses    
            }, f, indent=4)
        return self


if __name__ == '__main__':
    config = Configuration("", "", "")
    config.verify_ssh_to_github()