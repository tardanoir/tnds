import os
import subprocess

def main():
    if "{{ cookiecutter.include_django }}" == "yes":
        subprocess.run(["make", "setup_django"], check=True)
    
    # Initialize git repository
    subprocess.run(["git", "init"], check=True)
    
    # Create conda environment
    subprocess.run(["make", "environment"], check=True)

if __name__ == "__main__":
    main() 