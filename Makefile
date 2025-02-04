.PHONY: clean lint format sync_data_to_gcs sync_data_from_gcs requirements environment

# Project variables
PROJECT_NAME = {{ cookiecutter.project_slug }}
PYTHON_INTERPRETER = python
GCS_BUCKET = {{ cookiecutter.gcs_bucket }}

# Paths
DATA_DIR = data
PROCESSED_DATA = $(DATA_DIR)/processed
RAW_DATA = $(DATA_DIR)/raw

## Set up Python environment
environment:
	conda create --name $(PROJECT_NAME) python=3.10 -y
	conda init
	conda activate $(PROJECT_NAME) && pip install -r requirements.txt

## Install Python dependencies
requirements:
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using ruff
lint:
	ruff check .

## Format using ruff
format:
	ruff format .

## Sync data from GCS
sync_data_from_gcs:
	gsutil -m rsync -r gs://$(GCS_BUCKET)/$(PROJECT_NAME)/data/ $(DATA_DIR)/

## Sync data to GCS
sync_data_to_gcs:
	gsutil -m rsync -r $(DATA_DIR)/ gs://$(GCS_BUCKET)/$(PROJECT_NAME)/data/

## Set up Django project (only if include_django is yes)
{% if cookiecutter.include_django == 'yes' %}
setup_django:
	django-admin startproject web_app
	cd web_app && python manage.py startapp main
{% endif %} 