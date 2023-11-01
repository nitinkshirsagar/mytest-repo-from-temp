"""Python setup.py for mytest_repo_from_temp package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("mytest_repo_from_temp", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="mytest_repo_from_temp",
    version=read("mytest_repo_from_temp", "VERSION"),
    description="Awesome mytest_repo_from_temp created by nitinkshirsagar",
    url="https://github.com/nitinkshirsagar/mytest-repo-from-temp/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="nitinkshirsagar",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["mytest_repo_from_temp = mytest_repo_from_temp.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
