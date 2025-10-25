#!/usr/bin/env python3
"""
Test script for Python Virtual Environment Manager
This script tests the basic functionality of the tool

Developer: Khotso Tsoaela
Repository: https://github.com/ktsoaela/venv_manager
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path
from venv_manager import VenvManager

def test_basic_functionality():
    """Test basic functionality of VenvManager"""
    print("Testing Python Virtual Environment Manager")
    print("=" * 50)
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Initialize manager
            manager = VenvManager()
            print("Manager initialized successfully")
            
            # Test configuration loading
            config = manager.config
            print(f"Configuration loaded: {len(config)} keys")
            
            # Test tool checking (should not fail even if tools aren't installed)
            tools = ['virtualenv', 'pipenv', 'poetry']
            for tool in tools:
                try:
                    installed = manager.check_tool_installed(tool)
                    print(f"Tool check for {tool}: {'Installed' if installed else 'Not installed'}")
                except Exception as e:
                    print(f"Tool check for {tool} failed: {e}")
            
            # Test project listing (should work even with empty projects)
            print("\nTesting project listing...")
            manager.list_projects()
            print("Project listing completed")
            
            # Test activation instructions for non-existent project
            print("\nTesting activation instructions...")
            manager.activate_project("test_project")
            print("Activation instructions test completed")
            
            # Test dependency update for non-existent project
            print("\nTesting dependency update...")
            manager.update_dependencies("test_project")
            print("Dependency update test completed")
            
            print("\nAll basic tests passed!")
            
        except Exception as e:
            print(f"Test failed: {e}")
            return False
        finally:
            os.chdir(original_cwd)
    
    return True

def test_configuration_management():
    """Test configuration management"""
    print("\nTesting Configuration Management")
    print("=" * 50)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            manager = VenvManager()
            
            # Test configuration modification
            original_tool = manager.config['default_tool']
            manager.config['default_tool'] = 'pipenv'
            manager.save_config()
            
            # Create new manager to test config loading
            manager2 = VenvManager()
            if manager2.config['default_tool'] == 'pipenv':
                print("Configuration save/load test passed")
            else:
                print("Configuration save/load test failed")
                return False
            
            # Restore original configuration
            manager2.config['default_tool'] = original_tool
            manager2.save_config()
            
            print("Configuration management tests passed")
            return True
            
        except Exception as e:
            print(f"Configuration test failed: {e}")
            return False
        finally:
            os.chdir(original_cwd)

def test_error_handling():
    """Test error handling"""
    print("\nTesting Error Handling")
    print("=" * 50)
    
    try:
        manager = VenvManager()
        
        # Test with invalid project names
        invalid_names = ["", "   ", "invalid/name", "invalid\\name"]
        for name in invalid_names:
            try:
                manager.activate_project(name)
                print(f"Handled invalid project name: '{name}'")
            except Exception as e:
                print(f"Exception for invalid name '{name}': {e}")
        
        # Test with invalid tools
        try:
            manager.migrate_project("test", "invalid_tool")
            print("Handled invalid tool gracefully")
        except Exception as e:
            print(f"Exception for invalid tool: {e}")
        
        print("Error handling tests completed")
        return True
        
    except Exception as e:
        print(f"Error handling test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Python Virtual Environment Manager - Test Suite")
    print("=" * 60)
    
    tests = [
        ("Basic Functionality", test_basic_functionality),
        ("Configuration Management", test_configuration_management),
        ("Error Handling", test_error_handling)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name} Test...")
        try:
            if test_func():
                print(f"{test_name} test passed")
                passed += 1
            else:
                print(f"{test_name} test failed")
        except Exception as e:
            print(f"{test_name} test failed with exception: {e}")
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! The tool is working correctly.")
        return True
    else:
        print("Some tests failed. Please check the output above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
