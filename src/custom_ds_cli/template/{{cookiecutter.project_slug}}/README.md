# {{ cookiecutter.project_name }}

## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make environment` or `make lint`
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw           <- The original, immutable data dump
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks for exploration ONLY. Naming convention is
│                        `YYYYMMDD-initials-description.ipynb`
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports           <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures       <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│
├── src                <- Source code for use in this project
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
{% if cookiecutter.include_django == "yes" %}│
├── manage.py         <- Django's command-line utility for administrative tasks
└── {{ cookiecutter.project_slug }}  <- Django project directory
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py{% endif %}
```

## Setup

1. Create a conda environment:
```bash
make environment
```

2. Install dependencies:
```bash
make requirements
```

{% if cookiecutter.include_django == "yes" %}
3. Set up Django:
```bash
make setup_django
```
{% endif %}

## Development Workflow

1. Format code:
```bash
make format
```

2. Run linting:
```bash
make lint
```

{% if cookiecutter.gcs_bucket %}
## Data Synchronization

To sync data with GCS bucket:

```bash
# Download data from GCS
make sync_data_from_gcs

# Upload data to GCS
make sync_data_to_gcs
```
{% endif %}

## Project Guidelines

1. All exploratory work should be done in notebooks under the `notebooks/` directory
2. Production code goes in the `src/` directory
3. Use `ruff` for code formatting and linting
4. No Jupyter notebooks in version control except under `notebooks/`
5. Keep the data pipeline modular and documented 