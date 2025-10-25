#!/usr/bin/env python3
"""
Python Virtual Environment Manager
A comprehensive tool for managing Python virtual environments on Windows
Supports virtualenv, pipenv, and poetry with an interactive menu system

Developer: Khotso Tsoaela
Repository: https://github.com/ktsoaela/venv_manager
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path
from typing import Optional, Dict, List
import argparse

class VenvManager:
    def __init__(self):
        self.system = platform.system().lower()
        self.is_windows = self.system == 'windows'
        self.config_file = Path.home() / '.venv_manager_config.json'
        self.config = self.load_config()
        
    def load_config(self) -> Dict:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {
            'default_tool': 'virtualenv',
            'python_path': sys.executable,
            'projects': {}
        }
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def check_tool_installed(self, tool: str) -> bool:
        """Check if a tool is installed"""
        try:
            if tool == 'virtualenv':
                subprocess.run([sys.executable, '-m', 'virtualenv', '--version'], 
                             capture_output=True, check=True)
            elif tool == 'pipenv':
                subprocess.run(['pipenv', '--version'], 
                             capture_output=True, check=True)
            elif tool == 'poetry':
                subprocess.run(['poetry', '--version'], 
                             capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def install_tool(self, tool: str) -> bool:
        """Install a tool if not present"""
        if self.check_tool_installed(tool):
            return True
            
        print(f"Installing {tool}...")
        try:
            if tool == 'virtualenv':
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'virtualenv'], 
                             check=True)
            elif tool == 'pipenv':
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'pipenv'], 
                             check=True)
            elif tool == 'poetry':
                # Install poetry using the official installer
                if self.is_windows:
                    subprocess.run([
                        'powershell', '-Command', 
                        '(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -'
                    ], check=True)
                else:
                    subprocess.run([
                        'curl', '-sSL', 'https://install.python-poetry.org', '|', 'python3', '-'
                    ], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {tool}: {e}")
            return False
    
    def get_activation_script(self, venv_path: Path, tool: str) -> str:
        """Get the activation script path for different tools"""
        if tool == 'virtualenv':
            if self.is_windows:
                return str(venv_path / 'Scripts' / 'activate.bat')
            else:
                return str(venv_path / 'bin' / 'activate')
        elif tool == 'pipenv':
            return f"pipenv shell"
        elif tool == 'poetry':
            return f"poetry shell"
        return ""
    
    def create_virtualenv(self, name: str, python_version: Optional[str] = None) -> bool:
        """Create a virtual environment using virtualenv"""
        if not self.install_tool('virtualenv'):
            return False
            
        venv_path = Path.cwd() / name
        if venv_path.exists():
            print(f"Virtual environment '{name}' already exists!")
            return False
        
        try:
            cmd = [sys.executable, '-m', 'virtualenv', str(venv_path)]
            if python_version:
                cmd.extend(['-p', python_version])
            
            subprocess.run(cmd, check=True)
            
            # Save project info
            self.config['projects'][name] = {
                'tool': 'virtualenv',
                'path': str(venv_path),
                'created': str(Path.cwd())
            }
            self.save_config()
            
            print(f"Virtual environment '{name}' created successfully!")
            print(f"Location: {venv_path}")
            print(f"To activate: {self.get_activation_script(venv_path, 'virtualenv')}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")
            return False
    
    def create_pipenv(self, name: str, python_version: Optional[str] = None) -> bool:
        """Create a project using pipenv"""
        if not self.install_tool('pipenv'):
            return False
            
        project_path = Path.cwd() / name
        if project_path.exists():
            print(f"Project '{name}' already exists!")
            return False
        
        try:
            project_path.mkdir()
            os.chdir(project_path)
            
            cmd = ['pipenv', 'install']
            if python_version:
                cmd.extend(['--python', python_version])
            
            subprocess.run(cmd, check=True)
            
            # Save project info
            self.config['projects'][name] = {
                'tool': 'pipenv',
                'path': str(project_path),
                'created': str(project_path)
            }
            self.save_config()
            
            print(f"[OK] Pipenv project '{name}' created successfully!")
            print(f"[FOLDER] Location: {project_path}")
            print(f"[TOOL] To activate: cd {name} && pipenv shell")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to create pipenv project: {e}")
            return False
    
    def create_poetry(self, name: str, python_version: Optional[str] = None) -> bool:
        """Create a project using poetry"""
        if not self.install_tool('poetry'):
            return False
            
        try:
            cmd = ['poetry', 'new', name]
            subprocess.run(cmd, check=True)
            
            # Save project info
            project_path = Path.cwd() / name
            self.config['projects'][name] = {
                'tool': 'poetry',
                'path': str(project_path),
                'created': str(project_path)
            }
            self.save_config()
            
            print(f"[OK] Poetry project '{name}' created successfully!")
            print(f"[FOLDER] Location: {project_path}")
            print(f"[TOOL] To activate: cd {name} && poetry shell")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to create poetry project: {e}")
            return False
    
    def list_projects(self):
        """List all created projects"""
        if not self.config['projects']:
            print("No projects found.")
            return
        
        print("\n[LIST] Your Projects:")
        print("-" * 50)
        for name, info in self.config['projects'].items():
            tool = info['tool']
            path = info['path']
            print(f"[TOOL] {name} ({tool})")
            print(f"   [FOLDER] {path}")
            print()
    
    def activate_project(self, name: str):
        """Show activation instructions for a project"""
        if name not in self.config['projects']:
            print(f"Project '{name}' not found!")
            return
        
        info = self.config['projects'][name]
        tool = info['tool']
        path = info['path']
        
        print(f"\n[TOOL] Activating project '{name}' ({tool}):")
        print("-" * 40)
        
        if tool == 'virtualenv':
            if self.is_windows:
                print(f"Windows Command Prompt:")
                print(f"  {path}\\Scripts\\activate.bat")
                print(f"\nWindows PowerShell:")
                print(f"  {path}\\Scripts\\Activate.ps1")
            else:
                print(f"  source {path}/bin/activate")
        elif tool == 'pipenv':
            print(f"  cd {Path(path).name}")
            print(f"  pipenv shell")
        elif tool == 'poetry':
            print(f"  cd {Path(path).name}")
            print(f"  poetry shell")
    
    def update_dependencies(self, name: str):
        """Update dependencies for a project"""
        if name not in self.config['projects']:
            print(f"Project '{name}' not found!")
            return
        
        info = self.config['projects'][name]
        tool = info['tool']
        path = info['path']
        
        print(f"Updating dependencies for '{name}' ({tool})...")
        
        try:
            if tool == 'virtualenv':
                # For virtualenv, we need to activate and update
                if self.is_windows:
                    activate_script = Path(path) / 'Scripts' / 'activate.bat'
                    subprocess.run(f'"{activate_script}" && pip install --upgrade pip', 
                                 shell=True, check=True)
                else:
                    activate_script = Path(path) / 'bin' / 'activate'
                    subprocess.run(f'source "{activate_script}" && pip install --upgrade pip', 
                                 shell=True, check=True)
            elif tool == 'pipenv':
                os.chdir(path)
                subprocess.run(['pipenv', 'update'], check=True)
            elif tool == 'poetry':
                os.chdir(path)
                subprocess.run(['poetry', 'update'], check=True)
            
            print(f"[OK] Dependencies updated for '{name}'!")
            
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to update dependencies: {e}")
    
    def migrate_project(self, name: str, new_tool: str):
        """Migrate a project from one tool to another"""
        if name not in self.config['projects']:
            print(f"Project '{name}' not found!")
            return
        
        current_info = self.config['projects'][name]
        current_tool = current_info['tool']
        
        if current_tool == new_tool:
            print(f"Project '{name}' is already using {new_tool}!")
            return
        
        print(f"Migrating '{name}' from {current_tool} to {new_tool}...")
        print("[WARNING]  This will create a new project structure. Your code will be preserved.")
        
        confirm = input("Continue? (y/N): ").lower().strip()
        if confirm != 'y':
            print("Migration cancelled.")
            return
        
        # Get project name for new tool
        new_name = input(f"Enter new project name (default: {name}): ").strip() or name
        
        # Create new project
        if new_tool == 'virtualenv':
            success = self.create_virtualenv(new_name)
        elif new_tool == 'pipenv':
            success = self.create_pipenv(new_name)
        elif new_tool == 'poetry':
            success = self.create_poetry(new_name)
        else:
            print(f"Unknown tool: {new_tool}")
            return
        
        if success:
            print(f"[OK] Migration completed! New project: {new_name}")
            print("📝 Don't forget to copy your source code to the new project directory.")
    
    def interactive_menu(self):
        """Display interactive menu"""
        while True:
            print("\n" + "="*60)
            print("[PYTHON] Python Virtual Environment Manager")
            print("="*60)
            print("1. Create new virtual environment (virtualenv)")
            print("2. Create new project (pipenv)")
            print("3. Create new project (poetry)")
            print("4. List all projects")
            print("5. Show activation instructions")
            print("6. Update project dependencies")
            print("7. Migrate project to different tool")
            print("8. Install/Update tools")
            print("9. Settings")
            print("0. Exit")
            print("-"*60)
            
            choice = input("Choose an option (0-9): ").strip()
            
            if choice == '0':
                print("[GOODBYE] Goodbye!")
                break
            elif choice == '1':
                self.create_virtualenv_interactive()
            elif choice == '2':
                self.create_pipenv_interactive()
            elif choice == '3':
                self.create_poetry_interactive()
            elif choice == '4':
                self.list_projects()
            elif choice == '5':
                self.activate_project_interactive()
            elif choice == '6':
                self.update_dependencies_interactive()
            elif choice == '7':
                self.migrate_project_interactive()
            elif choice == '8':
                self.install_tools_interactive()
            elif choice == '9':
                self.settings_menu()
            else:
                print("[ERROR] Invalid option. Please try again.")
    
    def create_virtualenv_interactive(self):
        """Interactive virtualenv creation"""
        name = input("Enter virtual environment name: ").strip()
        if not name:
            print("[ERROR] Name cannot be empty!")
            return
        
        python_version = input("Enter Python version (optional, press Enter to use default): ").strip()
        if not python_version:
            python_version = None
        
        self.create_virtualenv(name, python_version)
    
    def create_pipenv_interactive(self):
        """Interactive pipenv creation"""
        name = input("Enter project name: ").strip()
        if not name:
            print("[ERROR] Name cannot be empty!")
            return
        
        python_version = input("Enter Python version (optional, press Enter to use default): ").strip()
        if not python_version:
            python_version = None
        
        self.create_pipenv(name, python_version)
    
    def create_poetry_interactive(self):
        """Interactive poetry creation"""
        name = input("Enter project name: ").strip()
        if not name:
            print("[ERROR] Name cannot be empty!")
            return
        
        self.create_poetry(name)
    
    def activate_project_interactive(self):
        """Interactive project activation"""
        if not self.config['projects']:
            print("No projects found.")
            return
        
        print("\nAvailable projects:")
        for i, name in enumerate(self.config['projects'].keys(), 1):
            print(f"{i}. {name}")
        
        try:
            choice = int(input("Select project number: ")) - 1
            project_names = list(self.config['projects'].keys())
            if 0 <= choice < len(project_names):
                self.activate_project(project_names[choice])
            else:
                print("[ERROR] Invalid selection!")
        except ValueError:
            print("[ERROR] Please enter a valid number!")
    
    def update_dependencies_interactive(self):
        """Interactive dependency update"""
        if not self.config['projects']:
            print("No projects found.")
            return
        
        print("\nAvailable projects:")
        for i, name in enumerate(self.config['projects'].keys(), 1):
            print(f"{i}. {name}")
        
        try:
            choice = int(input("Select project number: ")) - 1
            project_names = list(self.config['projects'].keys())
            if 0 <= choice < len(project_names):
                self.update_dependencies(project_names[choice])
            else:
                print("[ERROR] Invalid selection!")
        except ValueError:
            print("[ERROR] Please enter a valid number!")
    
    def migrate_project_interactive(self):
        """Interactive project migration"""
        if not self.config['projects']:
            print("No projects found.")
            return
        
        print("\nAvailable projects:")
        for i, name in enumerate(self.config['projects'].keys(), 1):
            print(f"{i}. {name}")
        
        try:
            choice = int(input("Select project number: ")) - 1
            project_names = list(self.config['projects'].keys())
            if 0 <= choice < len(project_names):
                project_name = project_names[choice]
                print(f"\nMigrate '{project_name}' to:")
                print("1. virtualenv")
                print("2. pipenv")
                print("3. poetry")
                
                tool_choice = input("Select tool (1-3): ").strip()
                tool_map = {'1': 'virtualenv', '2': 'pipenv', '3': 'poetry'}
                
                if tool_choice in tool_map:
                    self.migrate_project(project_name, tool_map[tool_choice])
                else:
                    print("[ERROR] Invalid selection!")
            else:
                print("[ERROR] Invalid selection!")
        except ValueError:
            print("[ERROR] Please enter a valid number!")
    
    def install_tools_interactive(self):
        """Interactive tool installation"""
        print("\nAvailable tools:")
        print("1. virtualenv")
        print("2. pipenv")
        print("3. poetry")
        print("4. All tools")
        
        choice = input("Select tool to install (1-4): ").strip()
        
        if choice == '1':
            self.install_tool('virtualenv')
        elif choice == '2':
            self.install_tool('pipenv')
        elif choice == '3':
            self.install_tool('poetry')
        elif choice == '4':
            for tool in ['virtualenv', 'pipenv', 'poetry']:
                self.install_tool(tool)
        else:
            print("[ERROR] Invalid selection!")
    
    def settings_menu(self):
        """Settings menu"""
        while True:
            print("\n" + "="*40)
            print("[SETTINGS]  Settings")
            print("="*40)
            print(f"Default tool: {self.config['default_tool']}")
            print(f"Python path: {self.config['python_path']}")
            print("-"*40)
            print("1. Change default tool")
            print("2. Change Python path")
            print("3. Reset configuration")
            print("0. Back to main menu")
            
            choice = input("Choose an option (0-3): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                print("\nAvailable tools:")
                print("1. virtualenv")
                print("2. pipenv")
                print("3. poetry")
                
                tool_choice = input("Select default tool (1-3): ").strip()
                tool_map = {'1': 'virtualenv', '2': 'pipenv', '3': 'poetry'}
                
                if tool_choice in tool_map:
                    self.config['default_tool'] = tool_map[tool_choice]
                    self.save_config()
                    print(f"[OK] Default tool set to {tool_map[tool_choice]}")
                else:
                    print("[ERROR] Invalid selection!")
            elif choice == '2':
                new_path = input(f"Enter new Python path (current: {self.config['python_path']}): ").strip()
                if new_path and Path(new_path).exists():
                    self.config['python_path'] = new_path
                    self.save_config()
                    print("[OK] Python path updated!")
                else:
                    print("[ERROR] Invalid path!")
            elif choice == '3':
                confirm = input("Are you sure you want to reset all settings? (y/N): ").lower().strip()
                if confirm == 'y':
                    self.config = {
                        'default_tool': 'virtualenv',
                        'python_path': sys.executable,
                        'projects': {}
                    }
                    self.save_config()
                    print("[OK] Configuration reset!")
            else:
                print("[ERROR] Invalid option!")

def main():
    parser = argparse.ArgumentParser(description='Python Virtual Environment Manager')
    parser.add_argument('command', nargs='?', help='Command to run (create, list, activate, update, migrate)')
    parser.add_argument('--name', '-n', help='Project/virtual environment name')
    parser.add_argument('--tool', '-t', choices=['virtualenv', 'pipenv', 'poetry'], 
                       help='Tool to use')
    parser.add_argument('--python', '-p', help='Python version to use')
    parser.add_argument('--interactive', '-i', action='store_true', 
                       help='Run in interactive mode')
    
    args = parser.parse_args()
    manager = VenvManager()
    
    if args.interactive or not args.command:
        manager.interactive_menu()
    elif args.command == 'create':
        if not args.name:
            print("[ERROR] Project name is required! Use --name or -n")
            return
        
        tool = args.tool or manager.config['default_tool']
        
        if tool == 'virtualenv':
            manager.create_virtualenv(args.name, args.python)
        elif tool == 'pipenv':
            manager.create_pipenv(args.name, args.python)
        elif tool == 'poetry':
            manager.create_poetry(args.name, args.python)
    elif args.command == 'list':
        manager.list_projects()
    elif args.command == 'activate':
        if not args.name:
            print("[ERROR] Project name is required! Use --name or -n")
            return
        manager.activate_project(args.name)
    elif args.command == 'update':
        if not args.name:
            print("[ERROR] Project name is required! Use --name or -n")
            return
        manager.update_dependencies(args.name)
    elif args.command == 'migrate':
        if not args.name or not args.tool:
            print("[ERROR] Project name and tool are required! Use --name and --tool")
            return
        manager.migrate_project(args.name, args.tool)
    else:
        print(f"[ERROR] Unknown command: {args.command}")
        parser.print_help()

if __name__ == '__main__':
    main()
