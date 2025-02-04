"""Post-project generation hooks."""
import os
import shutil
from pathlib import Path


def remove_django_files():
    """Remove Django-specific files if Django is not included."""
    project_dir = Path.cwd()
    project_slug = "{{ cookiecutter.project_slug }}"
    
    # List of files/directories to remove if Django is not included
    django_files = [
        "manage.py",
        project_slug,  # Django project directory
    ]
    
    for item in django_files:
        path = project_dir / item
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(path)


def main():
    """Main post-generation function."""
    if "{{ cookiecutter.include_django }}" == "no":
        remove_django_files()


if __name__ == "__main__":
    main() 