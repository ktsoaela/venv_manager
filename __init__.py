"""
Python Virtual Environment Manager

A comprehensive tool for managing Python virtual environments on Windows,
similar to Laravel's installer. This tool provides an interactive menu system
for creating and managing virtual environments using virtualenv, pipenv, and poetry.

Developer: Khotso Tsoaela
Repository: https://github.com/ktsoaela/venv_manager
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Khotso Tsoaela"
__email__ = ""
__repository__ = "https://github.com/ktsoaela/venv_manager"
__license__ = "MIT"

from .venv_manager_core import VenvManager

__all__ = ["VenvManager"]
