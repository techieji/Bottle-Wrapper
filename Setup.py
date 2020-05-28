import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="OblongBottle",
    version="0.0.1",
    description="Quickly create html and css document from the shell",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/techieji/Bottle-Wrapper",
    author="Pradhyum R",
    author_email="drpradhyum2016@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Wrapper"],
    include_package_data=True,
    install_requires=["bottle"],
)