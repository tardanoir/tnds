"""CLI for creating data science projects."""

import logging
import sys
from pathlib import Path

import click
import cookiecutter.main
import questionary
from packaging import version
from rich.console import Console
from rich.panel import Panel

TEMPLATE_PATH = Path(__file__).parent / "template"

console = Console()
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]


def validate_project_name(_, __, name):
    """Validate that the project name is a valid Python identifier."""
    if not name.isidentifier():
        return (
            "Project name must be a valid Python identifier "
            "(letters, numbers, underscore, not starting with number)"
        )
    return True


def get_project_config():
    """Interactive prompt for project configuration."""
    console.print(
        Panel.fit(
            "🐔 Welcome to Tardanoir's Data Science Project Generator 🐔",
            title="TNDS",
            border_style="blue",
        )
    )

    questions = [
        {
            "type": "text",
            "name": "project_name",
            "message": "What is your project name?",
            "validate": validate_project_name,
        },
        {
            "type": "select",
            "name": "python_version",
            "message": "Which Python version would you like to use?",
            "choices": PYTHON_VERSIONS,
            "default": "3.10",
        },
        {
            "type": "confirm",
            "name": "include_django",
            "message": "Would you like to include Django setup?",
            "default": False,
        },
        {
            "type": "text",
            "name": "gcs_bucket",
            "message": "Enter GCS bucket name for data sync (leave empty to skip):",
            "default": "",
        },
        {
            "type": "confirm",
            "name": "use_precommit",
            "message": "Would you like to set up pre-commit hooks?",
            "default": True,
        },
        {
            "type": "text",
            "name": "output_dir",
            "message": "Where should we create the project?",
            "default": ".",
        },
    ]

    answers = questionary.prompt(questions)

    if not answers:
        sys.exit(0)

    if answers["include_django"] and version.parse(
        answers["python_version"]
    ) < version.parse("3.10"):
        warning_msg = (
            "⚠️  Warning: Django 4.2+ requires Python 3.10 or higher. "
            "Do you want to continue anyway?"
        )
        if not questionary.confirm(warning_msg).ask():
            sys.exit(1)

    return answers


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Create a new data science project with an interactive setup."""
    if ctx.invoked_subcommand is None:
        try:
            config = get_project_config()

            context = {
                "project_name": config["project_name"],
                "include_django": "yes" if config["include_django"] else "no",
                "gcs_bucket": config["gcs_bucket"],
                "python_version": config["python_version"],
                "use_precommit": "yes" if config["use_precommit"] else "no",
            }

            console.print("\n🔧 Generating project with your configuration...\n")

            cookiecutter.main.cookiecutter(
                str(TEMPLATE_PATH),
                no_input=True,
                extra_context=context,
                output_dir=config["output_dir"],
            )

            project_path = Path(config["output_dir"]) / config["project_name"]
            pyproject_path = project_path / "pyproject.toml"

            with open(pyproject_path) as f:
                content = f.read()

            content = content.replace(
                'requires-python = ">=3.8"',
                f'requires-python = ">={config["python_version"]}"',
            )

            if config["include_django"]:
                django_deps = (
                    ',\n    "django>=4.2.0",'
                    '\n    "djangorestframework>=3.14.0"'
                    "\n]\n\n[project.optional-dependencies]"
                )
                content = content.replace(
                    "]\n\n[project.optional-dependencies]", django_deps
                )

            with open(pyproject_path, "w") as f:
                f.write(content)

            console.print("\n✨ Project successfully created! ✨\n", style="green bold")
            console.print("Next steps:")
            console.print("  1. cd", config["project_name"])
            console.print("  2. make environment    # Create conda environment")
            console.print("  3. make requirements   # Install dependencies")

            if config["include_django"]:
                console.print("  4. make setup_django   # Set up Django project")

        except Exception as e:
            console.print(f"\n❌ Error creating project: {str(e)}", style="red bold")
            sys.exit(1)


@cli.command("list")
def list_templates():
    """List available project templates and options."""
    console.print("\n📋 Available template options:\n")
    console.print(f"  • Python versions: {', '.join(PYTHON_VERSIONS)}")
    console.print("  • Optional Django integration")
    console.print("  • GCS bucket integration")
    console.print("  • Pre-commit hooks")
    console.print("  • Multiple license options\n")


if __name__ == "__main__":
    cli()
