# pipenv-shebang

*pipenv-shebang* allows you to put scripts in your path that run in a pipenv environment.

This solves the problem of launching `pipenv run script.py` from outside the script directory.

## Usage

Put this shebang at the top of your script:

```
#!/usr/bin/env pipenv-shebang
```

You can also run your script with

```
pipenv-shebang /path/to/script
```

## Installation

```
sudo pip install pipenv-shebang

# or
pip install --user pipenv-shebang
```
