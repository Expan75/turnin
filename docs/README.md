# turnin

Turnin is a cli-tool that aims to automate a git-first homework submission flow. In short, the tool sets up a homework repository for a given student and automates a submission flow which ends in a pull request being raised and instructors being notified.

## The Problem

Using a git provider like Github for homework submission has a ton of benefits but relies on students and instructors feeling comfortable with a git. Currently, there is no alternative to using Git and Github fully or not using it at all. This tool aims to be that in between without disabling the future fully fledged manual use of git and Github.

## Implications of the tool

For students this means:
1. Straight forward way of submitting work that can be done in a single command.
2. Ability to utilise repositories as templates for their submissions, reducing the amount of boilerplate that needs to be produced as part of any submission.
3. Practice with a terminal+editor based workflow and gain gradual exposure to the industry standard git approach of development.

For instructors this means:
1. No LMS is needed.
2. Automatic email notifications and timestamps upon submission.
3. Allows pull requests to be used as the basis of all feedback.
4. Usage of premade templates to standardise submissions (alt. running tests).

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
By this point, the homework is submitted, and the neccessary steps for raising a pull request with the content and assigned instructor will be taken care off.