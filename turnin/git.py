import os
import subprocess


def clone(repository_url: str, local_path: str = None):
    """Clone a github repository via system git tool"""
    command = f"git clone {repository_url}"
    command = command + f" {local_path}" if local_path is not None else command
    result = subprocess.run(command.split(" "), stdout=subprocess.PIPE)
    parsed_result = result.stdout.decode("utf-8")
    if "done" not in parsed_result:
        raise RuntimeError(f"Could not clone {repository_url}!")
    return parsed_result

    
def partial_clone(repository_url: str, local_path: str):
    """Like clone but removes the .git folder to avoid accidental submodules
        Does allow the equivilent of git clone github.com/user/reponame/repofolder
    """
    clone(repository_url, local_path)
    repository_top_level = os.listdir(local_path)


def prepare_remote_submission(
    local_repository_path: str, 
    submission_path: str,
    submission_name: str
):
    """Enables creating a pull request on a recently pushed update on a seperated assignment branch

        Equivilent of:
            mkdir submission_path
            echo "print('Hello, world')" >> submission_path/somefile.txt

            cp -r submission_path local_repository_path/<submission-name>
            cd local_repository_path
            git checkout -B <submission-name>
            git add . && git commit -am "TURNIN: add files for homework submission"
            git push -u origin <submission-name>
    """
    pass