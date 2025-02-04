"""Shared test fixtures and configuration."""
import os
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def clean_environment():
    """Clean up environment variables that might affect tests."""
    # Store original environment
    original_env = dict(os.environ)
    
    # Remove variables that might affect tests
    for var in ["DJANGO_SETTINGS_MODULE", "PYTHONPATH"]:
        os.environ.pop(var, None)
    
    yield
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary directory for project generation."""
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    yield tmp_path
    
    # Restore original working directory
    os.chdir(original_cwd) 