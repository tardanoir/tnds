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
pip install custom-ds-cli
```

## Usage

Create a new data science project:

```bash
tnds
```

This will start an interactive prompt to configure your project. You can also list available options:

```bash
tnds list
```

### Example Project Structure

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