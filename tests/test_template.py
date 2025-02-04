"""Tests for the project template functionality."""
import os
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter

from custom_ds_cli.cli import TEMPLATE_PATH


@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary directory for project generation."""
    os.chdir(tmp_path)
    return tmp_path


def test_template_basic_project(temp_project_dir):
    """Test creating a basic project without optional features."""
    # Create project using template
    project_name = "test_basic_project"
    cookiecutter(
        str(TEMPLATE_PATH),
        no_input=True,
        extra_context={
            "project_name": project_name,
            "include_django": "no",
            "gcs_bucket": "",
            "python_version": "3.10",
            "use_precommit": "no",
        },
        output_dir=str(temp_project_dir),
    )
    
    project_dir = temp_project_dir / project_name
    
    # Check basic structure
    assert project_dir.exists()
    assert (project_dir / "pyproject.toml").exists()
    assert (project_dir / "Makefile").exists()
    assert (project_dir / "README.md").exists()
    
    # Check data directories
    data_dir = project_dir / "data"
    assert (data_dir / "raw").exists()
    assert (data_dir / "processed").exists()
    assert (data_dir / "interim").exists()
    assert (data_dir / "external").exists()
    
    # Check source code structure
    src_dir = project_dir / "src"
    assert src_dir.exists()
    assert (src_dir / "__init__.py").exists()
    assert (src_dir / "data").exists()
    assert (src_dir / "features").exists()
    assert (src_dir / "models").exists()
    assert (src_dir / "visualization").exists()
    
    # Check that Django files are not present
    assert not (project_dir / "manage.py").exists()


def test_template_django_project(temp_project_dir):
    """Test creating a project with Django integration."""
    # Create project using template
    project_name = "test_django_project"
    cookiecutter(
        str(TEMPLATE_PATH),
        no_input=True,
        extra_context={
            "project_name": project_name,
            "include_django": "yes",
            "gcs_bucket": "",
            "python_version": "3.10",
            "use_precommit": "no",
        },
        output_dir=str(temp_project_dir),
    )
    
    project_dir = temp_project_dir / project_name
    
    # Check Django-specific files
    assert (project_dir / "manage.py").exists()
    assert (project_dir / project_name).exists()  # Django project directory
    assert (project_dir / project_name / "settings.py").exists()
    assert (project_dir / project_name / "urls.py").exists()
    assert (project_dir / project_name / "wsgi.py").exists()


def test_template_gcs_project(temp_project_dir):
    """Test creating a project with GCS integration."""
    # Create project using template
    project_name = "test_gcs_project"
    cookiecutter(
        str(TEMPLATE_PATH),
        no_input=True,
        extra_context={
            "project_name": project_name,
            "include_django": "no",
            "gcs_bucket": "test-bucket",
            "python_version": "3.10",
            "use_precommit": "no",
        },
        output_dir=str(temp_project_dir),
    )
    
    project_dir = temp_project_dir / project_name
    
    # Check Makefile for GCS commands
    makefile_path = project_dir / "Makefile"
    assert makefile_path.exists()
    
    makefile_content = makefile_path.read_text()
    assert "sync_data_from_gcs" in makefile_content
    assert "sync_data_to_gcs" in makefile_content
    assert "test-bucket" in makefile_content 