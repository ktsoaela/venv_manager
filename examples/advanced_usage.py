#!/usr/bin/env python3
"""
Advanced Usage Examples for Python Virtual Environment Manager
This file demonstrates advanced features and programmatic usage

Developer: Khotso Tsoaela
Repository: https://github.com/ktsoaela/venv_manager
"""

from venv_manager import VenvManager
import os
import json
from pathlib import Path

def demonstrate_advanced_features():
    """Demonstrate advanced features of the VenvManager"""
    manager = VenvManager()
    
    print("🔧 Advanced Usage Examples")
    print("=" * 50)
    
    # Example 1: Check tool availability
    print("\n1. Checking tool availability...")
    tools = ['virtualenv', 'pipenv', 'poetry']
    for tool in tools:
        installed = manager.check_tool_installed(tool)
        status = "✅ Installed" if installed else "❌ Not installed"
        print(f"   {tool}: {status}")
    
    # Example 2: Install missing tools
    print("\n2. Installing missing tools...")
    for tool in tools:
        if not manager.check_tool_installed(tool):
            print(f"   Installing {tool}...")
            success = manager.install_tool(tool)
            if success:
                print(f"   ✅ {tool} installed successfully")
            else:
                print(f"   ❌ Failed to install {tool}")
    
    # Example 3: Create project with specific Python version
    print("\n3. Creating project with specific Python version...")
    success = manager.create_virtualenv("advanced_project", "3.11")
    if success:
        print("   ✅ Advanced project created with Python 3.11")
    
    # Example 4: Update dependencies
    print("\n4. Updating project dependencies...")
    if "advanced_project" in manager.config['projects']:
        manager.update_dependencies("advanced_project")
    
    # Example 5: Show configuration
    print("\n5. Current configuration:")
    print(f"   Default tool: {manager.config['default_tool']}")
    print(f"   Python path: {manager.config['python_path']}")
    print(f"   Projects count: {len(manager.config['projects'])}")
    
    # Example 6: Migration example
    print("\n6. Project migration example...")
    if "advanced_project" in manager.config['projects']:
        print("   Migrating from virtualenv to pipenv...")
        # Note: This would create a new project, not modify the existing one
        # manager.migrate_project("advanced_project", "pipenv")
        print("   (Migration skipped in demo to avoid creating duplicate projects)")

def demonstrate_configuration_management():
    """Demonstrate configuration management features"""
    manager = VenvManager()
    
    print("\n⚙️ Configuration Management Examples")
    print("=" * 50)
    
    # Example 1: Change default tool
    print("\n1. Changing default tool...")
    original_tool = manager.config['default_tool']
    print(f"   Original default tool: {original_tool}")
    
    # Change to pipenv
    manager.config['default_tool'] = 'pipenv'
    manager.save_config()
    print(f"   New default tool: {manager.config['default_tool']}")
    
    # Restore original
    manager.config['default_tool'] = original_tool
    manager.save_config()
    print(f"   Restored to: {manager.config['default_tool']}")
    
    # Example 2: Add custom project metadata
    print("\n2. Adding custom project metadata...")
    if "advanced_project" in manager.config['projects']:
        project_info = manager.config['projects']['advanced_project']
        project_info['description'] = "Advanced Python project with custom features"
        project_info['tags'] = ['python', 'advanced', 'demo']
        project_info['created_by'] = "venv_manager_demo"
        manager.save_config()
        print("   ✅ Custom metadata added to project")
    
    # Example 3: Export project information
    print("\n3. Exporting project information...")
    projects_info = {}
    for name, info in manager.config['projects'].items():
        projects_info[name] = {
            'tool': info['tool'],
            'path': info['path'],
            'description': info.get('description', 'No description'),
            'tags': info.get('tags', []),
            'created_by': info.get('created_by', 'Unknown')
        }
    
    # Save to JSON file
    with open('projects_export.json', 'w') as f:
        json.dump(projects_info, f, indent=2)
    print("   ✅ Project information exported to projects_export.json")

def demonstrate_batch_operations():
    """Demonstrate batch operations"""
    manager = VenvManager()
    
    print("\n📦 Batch Operations Examples")
    print("=" * 50)
    
    # Example 1: Create multiple projects
    print("\n1. Creating multiple projects...")
    project_configs = [
        {'name': 'web_app', 'tool': 'poetry', 'python': '3.11'},
        {'name': 'data_analysis', 'tool': 'pipenv', 'python': '3.10'},
        {'name': 'simple_script', 'tool': 'virtualenv', 'python': '3.9'}
    ]
    
    for config in project_configs:
        print(f"   Creating {config['name']} with {config['tool']}...")
        if config['tool'] == 'virtualenv':
            success = manager.create_virtualenv(config['name'], config['python'])
        elif config['tool'] == 'pipenv':
            success = manager.create_pipenv(config['name'], config['python'])
        elif config['tool'] == 'poetry':
            success = manager.create_poetry(config['name'])
        
        if success:
            print(f"   ✅ {config['name']} created successfully")
        else:
            print(f"   ❌ Failed to create {config['name']}")
    
    # Example 2: Update all projects
    print("\n2. Updating all projects...")
    for project_name in manager.config['projects'].keys():
        print(f"   Updating {project_name}...")
        manager.update_dependencies(project_name)
    
    # Example 3: Show activation instructions for all projects
    print("\n3. Activation instructions for all projects...")
    for project_name in manager.config['projects'].keys():
        print(f"\n   Project: {project_name}")
        manager.activate_project(project_name)

def demonstrate_error_handling():
    """Demonstrate error handling and edge cases"""
    manager = VenvManager()
    
    print("\n🚨 Error Handling Examples")
    print("=" * 50)
    
    # Example 1: Try to create project with existing name
    print("\n1. Handling duplicate project names...")
    if "advanced_project" in manager.config['projects']:
        print("   Attempting to create duplicate project...")
        success = manager.create_virtualenv("advanced_project")
        if not success:
            print("   ✅ Properly handled duplicate project name")
    
    # Example 2: Try to activate non-existent project
    print("\n2. Handling non-existent project activation...")
    manager.activate_project("non_existent_project")
    
    # Example 3: Try to update non-existent project
    print("\n3. Handling non-existent project update...")
    manager.update_dependencies("non_existent_project")
    
    # Example 4: Try to migrate non-existent project
    print("\n4. Handling non-existent project migration...")
    manager.migrate_project("non_existent_project", "poetry")

def cleanup_demo_projects():
    """Clean up demo projects"""
    manager = VenvManager()
    
    print("\n🧹 Cleanup Demo Projects")
    print("=" * 50)
    
    demo_projects = [
        'example_venv', 'example_pipenv', 'example_poetry',
        'advanced_project', 'web_app', 'data_analysis', 'simple_script'
    ]
    
    for project_name in demo_projects:
        if project_name in manager.config['projects']:
            project_path = Path(manager.config['projects'][project_name]['path'])
            if project_path.exists():
                print(f"   Removing {project_name}...")
                # Note: In a real scenario, you'd want to be more careful about deletion
                # This is just for demo purposes
                print(f"   (Would remove: {project_path})")
            
            # Remove from config
            del manager.config['projects'][project_name]
    
    manager.save_config()
    print("   ✅ Demo projects cleaned up from configuration")

def main():
    """Main function to run all examples"""
    print("🐍 Python Virtual Environment Manager - Advanced Examples")
    print("=" * 70)
    
    try:
        demonstrate_advanced_features()
        demonstrate_configuration_management()
        demonstrate_batch_operations()
        demonstrate_error_handling()
        
        # Ask if user wants to cleanup
        print("\n" + "=" * 70)
        cleanup_choice = input("Do you want to cleanup demo projects? (y/N): ").lower().strip()
        if cleanup_choice == 'y':
            cleanup_demo_projects()
        
        print("\n🎉 Advanced examples completed!")
        print("You can now use the interactive menu with: python venv_manager.py")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Examples interrupted by user")
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")

if __name__ == "__main__":
    main()
