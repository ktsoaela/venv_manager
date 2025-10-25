# Contributing to Python Virtual Environment Manager

Thank you for your interest in contributing to the Python Virtual Environment Manager! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Development Workflow](#development-workflow)

## Code of Conduct

This project follows a code of conduct that we expect all contributors to adhere to. Please be respectful and constructive in all interactions.

## Getting Started

1. **Fork the repository** at [https://github.com/ktsoaela/venv_manager](https://github.com/ktsoaela/venv_manager)
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/venv_manager.git
   cd venv_manager
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites
- Python 3.7 or higher
- Git
- Windows (for testing Windows-specific features)

### Installation
```bash
# Clone the repository
git clone https://github.com/ktsoaela/venv_manager.git
cd venv_manager

# Install in development mode
pip install -e .

# Run tests
python test_venv_manager.py
```

### Project Structure
```
venv_manager/
├── venv_manager/           # Main package
│   ├── __init__.py
│   ├── main.py
│   └── venv_manager_core.py
├── examples/               # Example scripts
├── tests/                  # Test files
├── docs/                   # Documentation
├── venv.bat               # Windows batch wrapper
├── venv.ps1               # PowerShell wrapper
├── install.bat            # Windows installer
├── install.ps1            # PowerShell installer
├── setup.py               # Package setup
├── requirements.txt       # Dependencies
├── README.md              # Main documentation
├── QUICK_START.md         # Quick start guide
├── CHANGELOG.md           # Version history
└── CONTRIBUTING.md        # This file
```

## Contributing Guidelines

### What to Contribute
- Bug fixes
- New features
- Documentation improvements
- Test coverage improvements
- Performance optimizations
- Windows compatibility improvements

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Write clear and concise comments

### Commit Messages
Use clear and descriptive commit messages:
```
feat: add support for conda environments
fix: resolve Windows path issue in activation scripts
docs: update installation instructions
test: add tests for project migration functionality
```

### Testing
- Write tests for new features
- Ensure all existing tests pass
- Test on Windows (primary target platform)
- Test with different Python versions (3.7+)

## Pull Request Process

1. **Create a feature branch** from `main`
2. **Make your changes** following the coding guidelines
3. **Write tests** for your changes
4. **Update documentation** if needed
5. **Run the test suite** to ensure everything works
6. **Commit your changes** with clear messages
7. **Push to your fork** and create a pull request

### Pull Request Template
When creating a pull request, please include:

- **Description**: What changes were made and why
- **Type**: Bug fix, feature, documentation, etc.
- **Testing**: How the changes were tested
- **Breaking Changes**: Any breaking changes (if applicable)
- **Related Issues**: Link to any related issues

## Issue Reporting

### Before Creating an Issue
1. Check if the issue already exists
2. Search the documentation
3. Try the latest version

### Creating an Issue
When creating an issue, please include:

- **Description**: Clear description of the problem
- **Steps to Reproduce**: Detailed steps to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: OS, Python version, tool versions
- **Screenshots**: If applicable

### Issue Labels
- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to documentation
- `question`: Further information is requested
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed

## Development Workflow

### Feature Development
1. Create a feature branch
2. Implement the feature
3. Write tests
4. Update documentation
5. Test on Windows
6. Create pull request

### Bug Fixes
1. Create a bug fix branch
2. Identify and fix the bug
3. Write regression tests
4. Test the fix
5. Create pull request

### Documentation
1. Identify areas needing improvement
2. Update relevant files
3. Test documentation accuracy
4. Create pull request

## Code Review Process

All pull requests require review before merging:

1. **Automated Checks**: CI/CD pipeline runs tests
2. **Code Review**: At least one maintainer reviews the code
3. **Testing**: Changes are tested on Windows
4. **Approval**: Maintainer approves the changes
5. **Merge**: Changes are merged to main branch

## Release Process

1. Update version numbers
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Publish to PyPI (if applicable)

## Getting Help

- **Documentation**: Check README.md and QUICK_START.md
- **Issues**: Search existing issues or create a new one
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the maintainer if needed

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Python Virtual Environment Manager!**

**Developer**: Khotso Tsoaela  
**Repository**: [https://github.com/ktsoaela/venv_manager](https://github.com/ktsoaela/venv_manager)
