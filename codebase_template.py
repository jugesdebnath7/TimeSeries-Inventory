"""
        my_project/
        ├── .github/                           # GitHub Actions CI/CD
        │   └── workflows/
        │       ├── ci.yml                     # Continuous Integration Pipeline
        │       └── cd.yml                     # Continuous Deployment Pipeline
        ├── .gitlab-ci.yml                     # GitLab CI/CD (if using GitLab)
        ├── .env                                # Environment variables (loaded via dotenv)
        ├── .gitignore                          # Git ignores for dependencies, build artifacts, etc.
        ├── Dockerfile                          # Dockerfile to containerize the app
        ├── docker-compose.yml                  # Optional for orchestrating DB, Redis, etc.
        ├── config/                             # Configuration files (runtime, internal)
        │   ├── runtime.yaml                    # External runtime config
        │   ├── internal.yaml                   # Internal application config
        │   └── config_template.yaml            # Example config for users
        ├── data/                               # Data storage (raw, processed)
        │   ├── raw/                            # Raw data files
        │   └── processed/                      # Processed data files
        ├── notebooks/                          # Jupyter Notebooks (exploratory work)
        │   └── exploratory.ipynb
        ├── scripts/                            # Orchestration scripts
        │   ├── train_model.py                  # Training pipeline script
        │   └── ingest_data.py                  # One-off ingestion runner
        ├── src/                                # Main application code
        │   └── my_package/
        │       ├── __init__.py
        │       ├── main.py                     # FastAPI app entrypoint
        │       ├── config/                     # Configuration logic
        │       │   ├── __init__.py
        │       │   ├── loader.py               # Config loading utilities
        │       │   └── internal.yaml           # Internal config
        │       ├── ingestion/                  # Data ingestion logic
        │       │   ├── file_loader.py
        │       │   ├── api_loader.py
        │       │   └── db_loader.py
        │       ├── services/                   # Business logic and forecasting
        │       │   ├── inventory.py
        │       ├── models/                     # ML Models (ARIMA, LSTM)
        │       │   ├── arima.py
        │       │   └── lstm.py
        │       ├── utils/                      # Utility functions (logging, monitoring)
        │       │   ├── logger.py
        │       │   └── monitoring.py
        │       ├── api/                        # FastAPI API routes
        │       │   ├── v1/
        │       │   │   └── endpoints/
        │       │   │       └── inventory.py   # Forecast, train, etc. endpoints
        │       │   └── deps.py                 # Dependencies for API routes
        │       └── preprocessing/              # Data preparation and feature engineering
        │           ├── cleaning.py
        │           ├── validation.py
        │           └── feature_engineering.py
        ├── tests/                              # Test suite (unit & integration tests)
        │   ├── unit/                           # Unit tests for individual components
        │   │   ├── test_cleaning.py
        │   │   ├── test_validation.py
        │   │   └── test_feature_engineering.py
        │   ├── integration/                    # Integration tests for end-to-end workflow
        │   │   └── test_api.py                 # Testing FastAPI routes
        │   └── conftest.py                     # Fixtures and setup for tests
        ├── requirements.txt                    # Runtime dependencies
        ├── requirements-dev.txt                # Development dependencies (testing, linters, etc.)
        ├── setup.py                            # Packaging instructions for the app
        ├── pyproject.toml                      # Optional: Modern Python build system (e.g., poetry)
        └── README.md                           # Project documentation


"""

"""    ci.yml (Continuous Integration)

                name: CI

                on:
                push:
                branches:
                - main
                pull_request:
                branches:
                - main

                jobs:
                test:
                runs-on: ubuntu-latest
                steps:
                - uses: actions/checkout@v2
                - name: Set up Python
                        uses: actions/setup-python@v2
                        with:
                        python-version: '3.9'
                - name: Install dependencies
                        run: |
                        pip install -r requirements-dev.txt
                - name: Run Tests
                        run: |
                        pytest --maxfail=1 --disable-warnings -q
                - name: Lint Code
                        run: |
                        flake8 src/


"""
"""   cd.yml (Continuous Deployment)


                name: CD

                on:
                push:
                branches:
                - main

                jobs:
                deploy:
                runs-on: ubuntu-latest
                steps:
                - uses: actions/checkout@v2
                - name: Set up Docker
                        uses: docker/setup-buildx-action@v2
                - name: Log in to Docker Hub
                        uses: docker/login-action@v2
                        with:
                        username: ${{ secrets.DOCKER_USERNAME }}
                        password: ${{ secrets.DOCKER_PASSWORD }}
                - name: Build Docker image
                        run: |
                        docker build -t myusername/myproject .
                - name: Push Docker image to registry
                        run: |
                        docker push myusername/myproject
                - name: Deploy to Cloud/Server
                        run: |
                        ssh user@yourserver 'docker pull myusername/myproject && docker-compose up -d'



"""

import os
import logging
from pathlib import Path


# Project name set here
project_name = "timeseries_inventory"

# Define all project files and directories
files_list = [
    f".github/workflows/ci.yml",
    f".github/workflows/cd.yml",
    f".gitlab-ci.yml",
    f".env",
    f".gitignore",
    f"Dockerfile",
    f"docker-compose.yml",
    f"config/runtime.yaml",
    f"config/config_template.yaml",
    f"data/raw/",
    f"data/processed/",
    f"notebooks/exploratory.ipynb",
    f"scripts/train_model.py",
    f"scripts/ingest_data.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/main.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/loader.py",
    f"src/{project_name}/config/internal.yaml",
    f"src/{project_name}/ingestion/file_loader.py",
    f"src/{project_name}/ingestion/api_loader.py",
    f"src/{project_name}/ingestion/db_loader.py",
    f"src/{project_name}/services/inventory.py",
    f"src/{project_name}/models/arima.py",  # fixed typo from 'arimy.py'
    f"src/{project_name}/models/lstm.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/utils/monitoring.py",
    f"src/{project_name}/api/v1/endpoints/inventory.py",
    f"src/{project_name}/api/deps.py",
    f"src/{project_name}/preprocessing/cleaning.py",
    f"src/{project_name}/preprocessing/validation.py",
    f"src/{project_name}/preprocessing/feature_engineering.py",
    f"tests/unit/test_cleaning.py",
    f"tests/unit/test_validation.py",
    f"tests/unit/test_feature_engineering.py",
    f"tests/integration/test_api.py",
    f"tests/conftest_api.py",
    f"requirements.txt",
    f"requirements-dev.txt",
    f"setup.py",
    f"pyproject.toml",
]


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Logic to create files and directories
for file_list in files_list:
    file_path = Path(file_list)

    if file_list.endswith("/"):
        print(f"[DIR] Creating directory: {file_list}")
        file_path.mkdir(parents=True, exist_ok=True)
    else:
        print(f"[File] Creating file: {file_path}")
        if not file_path.parent.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            with open(file_path, "w") as f:
                f.write(f"#  {file_path.name} placeholder \n")




   


