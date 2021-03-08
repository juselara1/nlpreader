from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call

# requirements
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

# readme
with open("README.md", "r") as f:
    readme = f.read()

setup(
        name="nlpreader",
        version="1.0.0",
        author="Juan S. Lara",
        author_email="julara@unal.edu.co",
        packages=find_packages(),
        install_requires=requirements,
        description="Terminal reader that uses basic part of speech.",
        license="MIT",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/juselara1/nlpreader"
        )
