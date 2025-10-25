#!/bin/bash
# Python Virtual Environment Manager - Linux/macOS Shell Script
# This script provides easy access to the venv_manager tool
# Developer: Khotso Tsoaela
# Repository: https://github.com/ktsoaela/venv_manager

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the Python script with all arguments
python3 "$SCRIPT_DIR/venv_manager_core.py" "$@"
