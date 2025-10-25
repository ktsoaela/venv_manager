# Installation script for Python Virtual Environment Manager
# This script installs the tool and makes it available system-wide
# Developer: Khotso Tsoaela
# Repository: https://github.com/ktsoaela/venv_manager

Write-Host "Installing Python Virtual Environment Manager..." -ForegroundColor Green
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Installing package..." -ForegroundColor Yellow
Write-Host ""

# Install the package in development mode
try {
    pip install -e .
    Write-Host "Installation completed successfully!" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Installation failed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "You can now use the following commands:" -ForegroundColor Cyan
Write-Host "  venv                    - Run interactive menu" -ForegroundColor White
Write-Host "  venv create myproject   - Create new project" -ForegroundColor White
Write-Host "  venv list              - List all projects" -ForegroundColor White
Write-Host "  venv --help            - Show help" -ForegroundColor White
Write-Host ""
Write-Host "For PowerShell users, you can also use:" -ForegroundColor Cyan
Write-Host "  .\venv.ps1" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to continue"
