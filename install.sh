#!/bin/bash
# Installation script for Python Virtual Environment Manager
# This script installs the tool and makes it available system-wide
# Developer: Khotso Tsoaela
# Repository: https://github.com/ktsoaela/venv_manager

echo "Installing Python Virtual Environment Manager..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

echo "Python found: $(python3 --version)"
echo "Installing package..."
echo ""

# Install the package in development mode
if pip3 install -e .; then
    echo ""
    echo "Installation completed successfully!"
    echo ""
    echo "You can now use the following commands:"
    echo "  venv                    - Run interactive menu"
    echo "  venv create myproject   - Create new project"
    echo "  venv list              - List all projects"
    echo "  venv --help            - Show help"
    echo ""
    echo "For direct usage, you can also run:"
    echo "  python3 venv_manager_core.py"
    echo "  ./venv.sh"
    echo ""
else
    echo "ERROR: Installation failed"
    exit 1
fi
