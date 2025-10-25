@echo off
REM Installation script for Python Virtual Environment Manager
REM This script installs the tool and makes it available system-wide
REM Developer: Khotso Tsoaela
REM Repository: https://github.com/ktsoaela/venv_manager

echo Installing Python Virtual Environment Manager...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Python found. Installing package...
echo.

REM Install the package in development mode
pip install -e .

if errorlevel 1 (
    echo ERROR: Installation failed
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
echo.
echo You can now use the following commands:
echo   venv                    - Run interactive menu
echo   venv create myproject   - Create new project
echo   venv list              - List all projects
echo   venv --help            - Show help
echo.
echo For PowerShell users, you can also use:
echo   .\venv.ps1
echo.
pause
