"""Tests for the CLI functionality."""
import os
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from custom_ds_cli.cli import cli, validate_project_name


def test_validate_project_name():
    """Test project name validation."""
    # Valid project names
    assert validate_project_name(None, None, "valid_name") is True
    assert validate_project_name(None, None, "project123") is True
    assert validate_project_name(None, None, "MyProject") is True
    
    # Invalid project names
    assert validate_project_name(None, None, "123project") != True
    assert validate_project_name(None, None, "project-name") != True
    assert validate_project_name(None, None, "project name") != True


def test_cli_list_command():
    """Test the list command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["list"])
    assert result.exit_code == 0
    assert "Python versions" in result.output
    assert "Django integration" in result.output
    assert "GCS bucket integration" in result.output


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary directory for project generation."""
    os.chdir(tmp_path)
    return tmp_path


@patch("questionary.prompt")
def test_cli_project_creation(mock_prompt, temp_project_dir):
    """Test project creation with mocked user input."""
    mock_prompt.return_value = {
        "project_name": "test_project",
        "python_version": "3.10",
        "include_django": False,
        "gcs_bucket": "",
        "use_precommit": True,
        "output_dir": str(temp_project_dir),
    }
    
    runner = CliRunner()
    result = runner.invoke(cli)
    
    assert result.exit_code == 0
    assert "Project successfully created!" in result.output
    
    # Check if project directory was created
    project_dir = temp_project_dir / "test_project"
    assert project_dir.exists()
    
    # Check for essential files
    assert (project_dir / "pyproject.toml").exists()
    assert (project_dir / "Makefile").exists()
    assert (project_dir / "README.md").exists()
    
    # Check for source directories
    assert (project_dir / "src").exists()
    assert (project_dir / "src" / "data").exists()
    assert (project_dir / "src" / "features").exists()
    assert (project_dir / "src" / "models").exists()
    assert (project_dir / "src" / "visualization").exists() 