# turnin documentation

## Dependencies

1. Python>=3.8 -> [install python](https://www.python.org/downloads/)
1. Sign up to [Github](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)
2. Set up [SSH key authentication](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
3. Generate a [Github access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and copy it locally so you an reuse it (don't share it with anyone else!)

## Installation and setup

1. Install the library
    ```console
    python3 -m pip install turnin
    ```
2. Run the initialization to assign your email, token, and instructors to notify of submissions:
    ```console
    python3 -m turnin init 
    ```
3. Verify the installation and initialization:
    ```console
    python3 -m turnin verify
    ```

If no errors are returned, you are good to go!

## Usage

1. Create a new homework folder in which to put your submission files (you can optionally use a template for this!):
    ```console
    python3 -m turnin homework new --template github.com/org/repo --name my-homework-submission
    ```

2. Open the created homework submission folder in your favourite editor and work on your submission. When you feel done, submit it via the terminal:
    ```console
    python3 -m turnin homework submit my-homework-submission
    ```

# Motivation for the tool

## What?

A cli tool that ease the burden of introducing git to students unfamiliar with it, 
despite its benefits for both students (as it is the de facto development flow) and intructors (Pull requests vs. a local word doc file etc.).

## How?

With minimal setup (Github + SSH access + Github access token). The student flow would look something like:

1. Assuming Python is installed already, install the library via:
```console
python3 -m pip install turnin
```
2. Create new assignments, optionally based on provided templates by instructors (useful for standardisastion). Assignments here are just folders filled with files (usually code).
    ```console
    python3 -m turnin homework new --template github.com/org/template.git my-homework-folder
    ```
3. The student works on submission in whatever way they want, any tools, editors etc. are fine.

4. The student feels done and submits using the library. This automates the <code>git checkout -B submission-x && git add . && git commit -am && git push -u origin submission-x</code> flow. This happens in a local repository that is isolated from the actual my-homework-folder.
    ```console
    python3 -m turnin homework submit my-homework-foler
    ```

5. As part of the submission process, the assigned instructors will be tagged as reviewers on a raised pull request and notified accordingly.

6. When git has been introduced, it is easy to clone the existing homework repository and start the more manual flow, including cloning homework submission templates.

## Why?

1. Anyone with a computer with python, git and an authenticated Github will be able to automatically submit homework in an efficient manner without any knowledge of Git or programming language. This drastically simplifies the homework process for both students and instructors. This also comes at the benefit of 1) emulating a real work flow, 2) not locking into a LMS platform.

2. It is easy to gradually move into submitting "manually" via Git if we choose to. Simply manually fork a new course/homework template directory and do all the other steps manually. This lessens the cognitive load on students massively while still enabling to teach the "industry flow" of things. Training wheels come off when appropriate kind of thing.

3. Enforces a git first approach to content. The benefits are plentiful:
    - No need to rely on different email providers or message pro for persistance.
    - Submissions are always unique, standardised, traceable, and backed up.
    - Feedback can be given in the way its done in industry, including advanced features like writing highlighted code suggestions, line-by-line comments.
    - Submitting to git unlocks all sorts of automation, plagirism checking, semi-automated marking with human in the loop., etc.