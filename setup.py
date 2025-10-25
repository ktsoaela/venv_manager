#!/usr/bin/env python3
"""
Setup script for Python Virtual Environment Manager
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="venv-manager",
    version="1.0.0",
    author="Khotso Tsoaela",
    author_email="",
    description="A comprehensive tool for managing Python virtual environments on Windows, Linux, and macOS",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ktsoaela/venv_manager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "venv=venv_manager.main:main",
            "venv-manager=venv_manager.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.bat", "*.ps1", "*.md", "*.txt"],
    },
    keywords="python virtual environment venv pipenv poetry windows development",
    project_urls={
        "Bug Reports": "https://github.com/ktsoaela/venv_manager/issues",
        "Source": "https://github.com/ktsoaela/venv_manager",
        "Documentation": "https://github.com/ktsoaela/venv_manager#readme",
    },
)
