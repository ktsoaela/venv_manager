# 🐍 Python Virtual Environment Manager

A comprehensive tool for managing Python virtual environments on **Windows**, **Linux**, and **macOS**, similar to Laravel's installer. This tool provides an interactive menu system for creating and managing virtual environments using **virtualenv**, **pipenv**, and **poetry**.

**Developer:** Khotso Tsoaela  
**Repository:** [https://github.com/ktsoaela/venv_manager](https://github.com/ktsoaela/venv_manager)

## ✨ Features

- **Interactive Menu System**: Easy-to-use menu similar to Laravel's installer
- **Multiple Tool Support**: Works with virtualenv, pipenv, and poetry
- **Cross-Platform**: Works on Windows, Linux, and macOS with platform-specific optimizations
- **Project Management**: Track and manage multiple projects
- **Dependency Updates**: Easy dependency management and updates
- **Project Migration**: Migrate between different virtual environment tools
- **Auto-Installation**: Automatically installs required tools when needed

## 🚀 Quick Start

### Installation

1. **Download the tool**:
   ```bash
   git clone https://github.com/ktsoaela/venv_manager.git
   cd venv_manager
   ```

2. **Make it executable** (Platform-specific):
   
   **Windows:**
   ```cmd
   # For Command Prompt
   venv create myproject
   
   # For PowerShell
   .\venv.ps1 create myproject
   ```
   
   **Linux/macOS:**
   ```bash
   # Make scripts executable
   chmod +x venv.sh install.sh
   
   # Run the tool
   ./venv.sh create myproject
   ```

### Basic Usage

#### Interactive Mode (Recommended)
```bash
python venv_manager.py
# or
venv
# or
.\venv.ps1
```

#### Command Line Mode
```bash
# Create a virtual environment
venv create myproject --tool virtualenv

# Create a pipenv project
venv create myproject --tool pipenv

# Create a poetry project
venv create myproject --tool poetry

# List all projects
venv list

# Show activation instructions
venv activate myproject

# Update dependencies
venv update myproject

# Migrate project to different tool
venv migrate myproject --tool poetry
```

## 🛠️ Tool Comparison

| Feature | virtualenv | pipenv | poetry |
|---------|------------|--------|--------|
| **Ease of Use** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Dependency Management** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Lock Files** | ❌ | ✅ | ✅ |
| **Dependency Resolution** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Packaging** | ❌ | ❌ | ✅ |
| **Windows Support** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## 📋 Commands Reference

### Create Commands
```bash
# Create with virtualenv
venv create myproject --tool virtualenv --python 3.9

# Create with pipenv
venv create myproject --tool pipenv --python 3.9

# Create with poetry
venv create myproject --tool poetry
```

### Management Commands
```bash
# List all projects
venv list

# Show activation instructions
venv activate myproject

# Update project dependencies
venv update myproject

# Migrate project to different tool
venv migrate myproject --tool poetry
```

### Interactive Commands
```bash
# Run interactive menu
venv --interactive
# or simply
venv
```

## 🔧 Platform-Specific Features

### Activation Scripts
The tool provides platform-specific activation instructions:

**Windows:**
```cmd
# Command Prompt
myproject\Scripts\activate.bat

# PowerShell
myproject\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
# Bash/Zsh
source myproject/bin/activate

# Fish shell (macOS)
source myproject/bin/activate.fish
```

### Platform-Specific Setup

**Windows PowerShell Execution Policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Linux/macOS Permissions:**
```bash
# Make scripts executable
chmod +x venv.sh install.sh

# Install system-wide (optional)
sudo ./install.sh
```

## 📁 Project Structure

```
venv_manager/
├── venv_manager_core.py # Main Python script
├── venv.bat            # Windows batch file
├── venv.ps1            # PowerShell script
├── venv.sh             # Linux/macOS shell script
├── install.bat         # Windows installer
├── install.ps1         # PowerShell installer
├── install.sh          # Linux/macOS installer
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## ⚙️ Configuration

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

## 🎯 Use Cases

### 1. **Data Science Projects** (Recommended: Conda)
```bash
# For complex data science projects with non-Python dependencies
conda create -n myproject python=3.9
conda activate myproject
```

### 2. **Web Development** (Recommended: Poetry)
```bash
venv create mywebapp --tool poetry
cd mywebapp
poetry add fastapi uvicorn
```

### 3. **Simple Scripts** (Recommended: virtualenv)
```bash
venv create myscript --tool virtualenv
# Activate and install packages as needed
```

### 4. **Collaborative Projects** (Recommended: pipenv)
```bash
venv create ourproject --tool pipenv
cd ourproject
pipenv install requests
```

## 🔄 Migration Guide

### From virtualenv to pipenv
```bash
venv migrate myproject --tool pipenv
```

### From pipenv to poetry
```bash
venv migrate myproject --tool poetry
```

## 🐛 Troubleshooting

### Common Issues

1. **PowerShell Execution Policy**:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. **Python Not Found**:
   - Ensure Python is installed and in PATH
   - Use `--python` flag to specify Python path

3. **Tool Installation Fails**:
   - Check internet connection
   - Ensure pip is up to date: `python -m pip install --upgrade pip`

4. **Permission Errors**:
   - Run as administrator if needed
   - Check folder permissions

### Getting Help

```bash
# Show help
venv --help

# Show tool-specific help
python venv_manager.py --help
```

## 🤝 Contributing

1. Fork the repository at [https://github.com/ktsoaela/venv_manager](https://github.com/ktsoaela/venv_manager)
2. Create a feature branch
3. Make your changes
4. Test on Windows
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Developer:** Khotso Tsoaela
- Inspired by Laravel's elegant installer
- Built for the Python community
- Optimized for Windows development

---

**Happy Coding! 🐍✨**
