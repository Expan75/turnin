# turnin documentation

## What, How, and Why

Turnin is a cli-tool packaged as a standalone python library that automates the submission process of homework on Github. It is meant to be used by students submitting programming assignmnets, and be benefitted by instructors being able to review these assignments as they would any other code.

In short, a remote repository is maintained and updated when the student submits. The files are moved to the "hidden" repository (created under ~/.turnin) and committed+pushed to a new branch (and a pull request is automatically raised with the appropriate reviewers).

This accomplishes:

1. The student is can learn git at the their own pace.
2. The submission is standardised, repeatable, and developer centric.
3. The review process is standardised and feedback is available as soon as it is released.
4. Both students and instructors work within the industry standard developer flow.

## Dependencies

1. Python>=3.8 -> [install python](https://www.python.org/downloads/)
2. Sign up to [Github](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)
3. Set up [SSH key authentication](https://docs.github.com/en/authentication/connecting-to-github-with-ssh). This step is optional if you allow the tool to generate ssh keys for you.

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

## Bugs and Issues

Please do make use of the issues and report bugs if you find any!

## Contributing

To contribute, fork the repository and create a pull request of your feature. To run the tool locally, you'll need to create a new [Github app](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps), get the client ID, and proceed to clone the repostiory. 

Make sure to supply the <code>GITHUB_APP_CLIENT_ID</code> as an environment variable and run the tool like:

```console
export GITHUB_APP_CLIENT_ID="..."
python3 -m turnin # run the tool
python3 -m unittest # run tests
```