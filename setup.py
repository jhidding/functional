#!/usr/bin/env python

from setuptools import setup

test_deps = [
    "pytest>=5,<6",
    "pytest-cov>=2.8.1,<3",
    "pytest-mypy>=0.4.2,<1",
    "pytest-flake8>=1.0,<2",
    "flake8>=3,<4"]

setup(
    name="functional",
    version="0.1.0",
    py_modules=["auto_shelve", "decorator"],
    install_requires=[],
    tests_require=test_deps,
    extras_require={
        "test": test_deps
    },
    # include_package_data=True,
    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.txt', '*.rst'],
    #     # And include any *.msg files found in the 'hello' package, too:
    #     'hello': ['*.msg'],
    # },

    # metadata to display on PyPI
    author="Johan Hidding",
    author_email="j.hidding@esciencecenter.nl",
    description="Functional programming tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # could also include long_description, download_url, etc.
)
