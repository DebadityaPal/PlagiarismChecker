# For Contributors

## Tech Stack

The entire OCR and Plagiarism Checking modules have been coded in Python. Some libraries used are:

1. OpenCV
2. Tensorflow
3. GoogleSearch API

The website backend has been made using Django, the APIs have been made using the REST framework.
The website frontend has been made using React.js.

Contributions are welcome in all the modules of the project: OCR, Plagiarism Checker as well as Website.


## Issues for new contributors
While we welcome any form of contribution, we've marked a few issues which are particularly suited for new contributors. These issues are marked with the `good first issue` label. Other issues are also marked according to their difficulty level.

## How to contribute
If you would like to work on an issue, please follow these guidelines:
* Ask one of the maintainers to assign the issue to you, and feel free to ask any questions to clarify the issue
* Fork this repository to your GitHub account by clicking on the 'Fork' button at the top-right of the page
* Clone your fork of the repository to your local machine
* Enter the directory of the repository, and follow the installation instructions given in the README
* Create a new branch to hold your changes, and name your branches according to the issue you're working on

`git checkout -b your-new-branch-name`

* Make your changes to the code and try to resolve the issue. Make sure you add descriptive comments and variable names, so that it becomes easier for everyone else to understand your code
* Now, stage your changes with

`git add .`

* Commit your changes, and ensure that your commit message describes the changes you have made in your code. Commit messages should preferably be in the imperative mood, such as "add documentation" or "modify README" instead of in the past tense. You can commit your changes and add a message by running

`git commit -m "your commit message goes here"`

* That's all! Now, you just need to push your changes to your repository with

`git push -u origin your-new-branch-name`


## Opening a pull request
If you're working on an issue, and would like to submit a pull request, please follow these guidelines:
* Visit your fork of the repository, and click on the 'Pull Request' button that would be appearing on top of the page
* Mention the changes in the PR in the title briefly
* Mention the issue number that this PR will resolve in the description so as to automatically close the issue when the PR is merged
* Describe your changes in the PR description, and feel free to give examples or code samples
* If you would like to continue working on your PR, and mark it as a work in progress, you can submit a draft PR instead

## Linting

The entire project is linted using `black` and `flake8`, so any pull requests must be subjected to the necessary linting. For VSCode users, you can copy the following linting settings

```
{
"python.formatting.provider": "black",
"python.linting.flake8Enabled": true,
"python.linting.flake8Path": "flake8",
"python.linting.flake8Args": [
"--max-line-length=80",
"--select=B,C,E,F,W,B950",
"--ignore=E203,E501,W503"
],
"python.linting.pylintEnabled": false,
"python.linting.enabled": true,
}
```
