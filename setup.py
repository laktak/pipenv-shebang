from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    readme = f.read()

if os.path.exists("/bin/bash"):
    scripts = ["bash/pipenv-shebang"]
else:
    scripts = ["py/pipenv-shebang"]

setup(
    name="pipenv-shebang",
    version="0.0.4",
    url="https://github.com/laktak/pipenv-shebang",
    author="Christian Zangl",
    author_email="laktak@cdak.net",
    description="pipenv-shebang allows you to put scripts in your path that run in a pipenv environment.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=[],
    install_requires=[],
    scripts=scripts,
    data_files=[("py", ["py/pipenv-shebang"]), ("bash", ["bash/pipenv-shebang"])],
)
