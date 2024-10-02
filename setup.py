import pathlib
import os

from setuptools import find_packages, setup

import py2exe

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

github_token: str = os.environ["GITHUB_TOKEN"]

setup(
    name="json-merger",
    version="1.0.0",
    description="Faraday JSON merger used by production.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bang & Olufsen A/S",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic  :: Software development :: Test tools",
        "Programming language :: Python :: 3.10",
    ],
    packages=find_packages(include=["json-merger", "json-merger.*"]),
    python_requires=">=3.10, <4",
    install_requires=[
        "click",
        "colorama",
    ],
    console=["json_merger.main.py",]
)
