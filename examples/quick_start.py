#!/usr/bin/env python3
"""
Quick Start Examples for Python Virtual Environment Manager
This file demonstrates how to use the tool programmatically

Developer: Khotso Tsoaela
Repository: https://github.com/ktsoaela/venv_manager
"""

from venv_manager import VenvManager
import os

def main():
    # Initialize the manager
    manager = VenvManager()
    
    print("🐍 Python Virtual Environment Manager - Quick Start Examples")
    print("=" * 60)
    
    # Example 1: Create a virtualenv project
    print("\n1. Creating a virtualenv project...")
    success = manager.create_virtualenv("example_venv", "3.9")
    if success:
        print("✅ Virtualenv project created!")
    
    # Example 2: Create a pipenv project
    print("\n2. Creating a pipenv project...")
    success = manager.create_pipenv("example_pipenv", "3.9")
    if success:
        print("✅ Pipenv project created!")
    
    # Example 3: Create a poetry project
    print("\n3. Creating a poetry project...")
    success = manager.create_poetry("example_poetry")
    if success:
        print("✅ Poetry project created!")
    
    # Example 4: List all projects
    print("\n4. Listing all projects...")
    manager.list_projects()
    
    # Example 5: Show activation instructions
    print("\n5. Activation instructions for virtualenv project...")
    manager.activate_project("example_venv")
    
    print("\n" + "=" * 60)
    print("🎉 Quick start examples completed!")
    print("You can now use the interactive menu with: python venv_manager.py")

if __name__ == "__main__":
    main()
