# 🚀 Quick Start Guide

**Developer:** Khotso Tsoaela  
**Repository:** [https://github.com/ktsoaela/venv_manager](https://github.com/ktsoaela/venv_manager)  
**Platforms:** Windows, Linux, macOS

## Installation

### Option 1: Direct Usage (Recommended)
```bash
# Clone the repository
git clone https://github.com/ktsoaela/venv_manager.git
cd venv_manager

# Then run directly:
python venv_manager_core.py
```

### Option 2: Install as Package

**Windows:**
```bash
# Install in development mode
pip install -e .

# Or use the Windows installer
install.bat
# or
.\install.ps1
```

**Linux/macOS:**
```bash
# Install in development mode
pip3 install -e .

# Or use the Linux/macOS installer
chmod +x install.sh
./install.sh
```

## Basic Usage

### Interactive Mode (Easiest)

**Windows:**
```bash
python venv_manager_core.py
# or
venv
# or
.\venv.ps1
```

**Linux/macOS:**
```bash
python3 venv_manager_core.py
# or
./venv.sh
```

### Command Line Mode
```bash
# Create a virtual environment
python venv_manager_core.py create --name myproject --tool virtualenv

# Create a pipenv project
python venv_manager_core.py create --name myproject --tool pipenv

# Create a poetry project
python venv_manager_core.py create --name myproject --tool poetry

# List all projects
python venv_manager_core.py list

# Show activation instructions
python venv_manager_core.py activate --name myproject

# Update dependencies
python venv_manager_core.py update --name myproject
```

## Windows-Specific Usage

### Command Prompt
```cmd
# Run the tool
venv.bat

# Create project
venv.bat create --name myproject --tool virtualenv
```

### PowerShell
```powershell
# Run the tool
.\venv.ps1

# Create project
.\venv.ps1 create --name myproject --tool virtualenv
```

## Tool Comparison

| Feature | virtualenv | pipenv | poetry |
|---------|------------|--------|--------|
| **Ease of Use** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Dependency Management** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Lock Files** | ❌ | ✅ | ✅ |
| **Packaging** | ❌ | ❌ | ✅ |
| **Windows Support** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## Common Commands

### Create Projects
```bash
# Simple virtual environment
python venv_manager_core.py create --name webapp --tool virtualenv

# Data science project with pipenv
python venv_manager_core.py create --name datascience --tool pipenv --python 3.11

# Web application with poetry
python venv_manager_core.py create --name myapi --tool poetry
```

### Manage Projects
```bash
# List all projects
python venv_manager_core.py list

# Show how to activate a project
python venv_manager_core.py activate --name webapp

# Update project dependencies
python venv_manager_core.py update --name webapp

# Migrate project to different tool
python venv_manager_core.py migrate --name webapp --tool poetry
```

## Activation Instructions

### virtualenv
```cmd
# Command Prompt
myproject\Scripts\activate.bat

# PowerShell
myproject\Scripts\Activate.ps1
```

### pipenv
```bash
cd myproject
pipenv shell
```

### poetry
```bash
cd myproject
poetry shell
```

## Troubleshooting

### PowerShell Execution Policy
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python Not Found
- Ensure Python is installed and in PATH
- Use `--python` flag to specify Python path

### Tool Installation Fails
- Check internet connection
- Update pip: `python -m pip install --upgrade pip`

## Examples

### Example 1: Web Development
```bash
# Create a FastAPI project
python venv_manager_core.py create --name fastapi-app --tool poetry
cd fastapi-app
poetry add fastapi uvicorn
poetry shell
```

### Example 2: Data Science
```bash
# Create a data science project
python venv_manager_core.py create --name data-analysis --tool pipenv --python 3.11
cd data-analysis
pipenv install pandas numpy matplotlib jupyter
pipenv shell
```

### Example 3: Simple Scripts
```bash
# Create a simple script environment
python venv_manager_core.py create --name my-scripts --tool virtualenv
# Activate and install packages as needed
```

## Getting Help

```bash
# Show help
python venv_manager_core.py --help

# Show specific command help
python venv_manager_core.py create --help
```

## Configuration

The tool automatically creates a configuration file at `~/.venv_manager_config.json`:

```json
{
  "default_tool": "virtualenv",
  "python_path": "C:\\Python39\\python.exe",
  "projects": {
    "myproject": {
      "tool": "virtualenv",
      "path": "C:\\Work\\myproject",
      "created": "C:\\Work"
    }
  }
}
```

## Next Steps

1. **Try the interactive mode**: `python venv_manager_core.py`
2. **Create your first project**: Choose option 1, 2, or 3
3. **Explore the features**: List projects, show activation instructions
4. **Read the full documentation**: Check `README.md` for detailed information

**Developer:** Khotso Tsoaela  
**Repository:** [https://github.com/ktsoaela/venv_manager](https://github.com/ktsoaela/venv_manager)

Happy coding! 🐍
