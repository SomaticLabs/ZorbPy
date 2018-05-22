from setuptools import Command
from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="zorb",
    version="0.1.5",
    author="Somatic Labs",
    author_email="developers@somaticlabs.io",
    description="Python SDK for the Zorb Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SomaticLabs/ZorbPy",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    ),
)
