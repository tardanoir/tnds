"""Post-generation hook for setting up the project."""
import subprocess


def main():
    """Run post-generation tasks."""
    if "{{ cookiecutter.include_django }}" == "yes":
        subprocess.run(["make", "setup_django"], check=True)
    
    # Initialize git repository
    subprocess.run(["git", "init"], check=True)
    
    # Create conda environment
    subprocess.run(["make", "environment"], check=True)

if __name__ == "__main__":
    main() 