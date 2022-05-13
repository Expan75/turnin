# Development plan for cli tool

## Why?

1. Anyone with a computer with python, git and an authenticated github account (hard to avoid without sacrificing privacy) will be able to automatically submit homework in an efficient manner without any knowledge of Git or programming language. This drastically simplifies the homework process for both students and instructors.

2. It is easy to gradually move into submitting "manually" via Git if we choose to. Simply manually fork a new course/homework template directory and do all the other steps manually. This lessens the cognitive load on students massively while still enabling to teach the "industry flow" of things. Training wheels come off when appropriate kind of thing.

3. Enforces a git first approach to content. The benefits are plentiful:
- No need to pay for preemium slack as a file storage solution.
- No need to rely on different email providers for persistance.
- Submissions are always unique, standardised, traceable, and backed up.
- Submitting to git unlocks all sorts of autiomation, plagirism checking, semi-automated marking with human in the loop., etc.

## Requirements

1. As a student, I want to be make sure that I have setup everything correctly.

    ```console
    # checks ~/.cfg github token
    python -m cfg validate
    ```

2. As a student, I want to be able to fork and clone a remote repository based of a template repository using a single command. 

    ```console
    python -m cfg homework create
    ```

3. As a student I want to control the lifecycle of homework via simple commands.
    
    ```console 
    python -m cfg homework create|list|describe|submit
    ```

4. As a student I want add who my assigned instructor(s) are via the cli

    ```console
    python -m cfg assign erik.hakansson96@gmail.com
    ```

5. As an intructor I want to be notified when a student submits homework.

    - No manual assigning as collaborator/reviewer should be required for any party.

5. As an Instructor (Disaster recovery), I want to be able to handle the event of the structure/tool breaking, switch over to manual git control, and then switch back to tool.

## Questions marks

1. Is it better to have a single fullstack homework repo, or one for each assignment? Disaster recovery and blast radius vs. clutter/complexity?
    - unclear but we're running with a single one. Managing permissions on more becomes cumbersome.

2. Some state is required locally, e.g.:
    - assigned instructor(s)
    - student name, cohort, etc. (throw in a uuid for good measure).

    This should preferebly be stored in a .cfg in /home/.

## Misc. Notes

Biggest hurdle: authenticaiton -> solution GitHub access token

1. cfg init # create a new directory in a standardised place mkdir e.g. ~/cfg
2. cfg homework init --name fullstack sql-week1 # clone homework submission template and stuff it in namespace <code>~/cfg/$course/$homework/$name</code>
3. cfg homework submit --name fullstack week1 # branch+add+commit+pushes everything to the target repository and creates a PR AND tags an instructor.

- Potential to expand namespaces to cover more courses, assignments (theory questions, assessments).
- Requirements on the student side: not mess up folder hierarchy and use appropriate commands to submit.
- Requirements on the instructor side: mark via PR.