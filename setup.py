from setuptools import Command
from setuptools import find_packages
from setuptools import setup

from subprocess import call

class BluefruitLEInstallCommand(Command):
    user_options = []

    def initialize_options(self):
        """Abstract method that is required to be overwritten"""

    def finalize_options(self):
        """Abstract method that is required to be overwritten"""

    def run(self):
        call(["git", "clone", "https://github.com/adafruit/Adafruit_Python_BluefruitLE.git"])
        call(["cd", "Adafruit_Python_BluefruitLE"])
        call(["python", "setup.py", "install"])
        call(["cd", ".."])

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="zorb",
    version="0.1.2",
    author="Somatic Labs",
    author_email="developers@somaticlabs.io",
    description="Python SDK for the Zorb Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SomaticLabs/ZorbPy",
    packages=find_packages(),
    cmdclass={'bluefruitLE': BluefruitLEInstallCommand},
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
    ),
)
