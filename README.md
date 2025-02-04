# Custom Data Science Project Generator

A CLI tool for generating standardized data science project templates with best practices built-in.

## Features

- Standardized data science project structure
- Optional Django integration
- GCS bucket integration for data sync
- Pre-commit hooks with ruff for code quality
- Makefile with common commands
- Separation of exploration and production code
- No Jupyter notebooks in version control by default

## Installation

```bash
pip install -e .
```

## Usage

Create a new data science project:

```bash
create-ds my_project
```

### Options

- `--django`: Include Django setup
- `--gcs-bucket TEXT`: GCS bucket name for data sync
- `--output-dir TEXT`: Where to output the project (default: current directory)
- `--python-version [3.10|3.11]`: Python version to use (default: 3.10)
- `--no-precommit`: Skip pre-commit hooks setup

### Example

```bash
create-ds my_project --python-version 3.11 --django --gcs-bucket my-bucket
```

## Project Structure

The generated project will have the following structure:

```
├── data/               <- Data files
│   ├── external/      <- Data from third party sources
│   ├── interim/       <- Intermediate data
│   ├── processed/     <- Final, canonical data sets
│   └── raw/          <- Original, immutable data
├── models/            <- Trained models
├── notebooks/         <- Jupyter notebooks (for exploration only)
├── references/        <- Data dictionaries, manuals, etc.
├── reports/           <- Generated analysis
│   └── figures/      <- Generated graphics and figures
└── src/               <- Source code
    ├── data/         <- Scripts to process data
    ├── features/     <- Feature engineering code
    ├── models/       <- Model training and prediction
    └── visualization/<- Analysis and reporting scripts
```

## Development

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Install pre-commit hooks:
```bash
pre-commit install
```

3. Run linting:
```bash
ruff check .
```

4. Format code:
```bash
ruff format .
``` 