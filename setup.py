#!/usr/bin/env python
"""scrapli_asyncssh - asyncssh transport plugin for scrapli"""
import setuptools

from scrapli_asyncssh import __version__

__author__ = "Carl Montanari"

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="scrapli_asyncssh",
    version=__version__,
    author=__author__,
    author_email="carl.r.montanari@gmail.com",
    description="asyncssh transport plugin for the scrapli SSH|Telnet screen scraping library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scrapli/scrapli_asyncssh",
    packages=setuptools.find_packages(),
    install_requires=["scrapli>=2020.06.06", "asyncssh>=2.2.1"],
    extras_require={},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)
