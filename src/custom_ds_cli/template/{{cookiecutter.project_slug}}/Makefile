.PHONY: clean environment requirements lint format sync_data_to_gcs sync_data_from_gcs

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = {{ cookiecutter.project_slug }}
PYTHON_VERSION = {{ cookiecutter.python_version }}
CONDA_ENV = $(PROJECT_NAME)

ifeq ($(shell uname),Darwin)
    CONDA_PLATFORM = osx-64
else ifeq ($(shell uname),Linux)
    CONDA_PLATFORM = linux-64
endif

# Define SHELL to use conda activate
SHELL := /bin/bash

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up conda environment
environment:
	@echo "Creating conda environment..."
	conda create --name $(CONDA_ENV) python=$(PYTHON_VERSION) -y
	conda init 
	@echo "To activate the environment, run:"
	@echo "conda activate $(CONDA_ENV)"
	@echo "Then install the dependencies with:"
	@echo "make requirements"

## Install Python dependencies
requirements:
	@if [ "$(CONDA_DEFAULT_ENV)" != "$(CONDA_ENV)" ]; then \
		echo "Please activate the conda environment first:"; \
		echo "conda activate $(CONDA_ENV)"; \
		exit 1; \
	fi
	pip install -e ".[dev]"
	{% if cookiecutter.use_precommit == "yes" %}
	pre-commit install
	{% endif %}

## Delete all generated files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

## Format code with ruff
format:
	ruff format .
	ruff check . --fix

## Lint using ruff
lint:
	ruff check .

{% if cookiecutter.gcs_bucket %}
## Sync data from GCS
sync_data_from_gcs:
	gsutil -m rsync -r gs://{{ cookiecutter.gcs_bucket }}/data/ data/

## Sync data to GCS
sync_data_to_gcs:
	gsutil -m rsync -r data/ gs://{{ cookiecutter.gcs_bucket }}/data/
{% endif %}

{% if cookiecutter.include_django == "yes" %}
## Set up Django project
setup_django:
	python manage.py migrate
	python manage.py createsuperuser
{% endif %}

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

help:
	@echo "$$(tput bold)Available commands:$$(tput sgr0)"
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' 