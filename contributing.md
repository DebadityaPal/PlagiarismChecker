# For Contributors

## Tech Stack

The entire OCR and Plagiarism Checking modules have been coded in Python. Some libraries used are:

1. OpenCV
2. Tensorflow
3. GoogleSearch API

The website backend has been made using Django, the APIs have been made using the REST framework.
The website frontend has been made using React.js.

Contributions are welcome in all the modules of the project: OCR, Plagiarism Checker as well as Website.

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
