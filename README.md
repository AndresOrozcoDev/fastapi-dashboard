# FastAPI Dashboard

Endpoints RestFull API's for User dashboard panel.

## Requirements

Make sure you have the following programs installed before running the application:

- [Python (v3.11.5)](https://www.python.org/downloads/release/python-3115/)

## Development server

Install virtual environment
```bash
  pip install virtualenv
```

Create virtual environment

```bash
  python -m venv env
```

Activate virtual environment

```bash
  env\Scripts\activate
```

Install requirements.txt file

```bash
  pip install -r requirements.txt
```

Create requirements.txt file

```bash
  pip freeze > requirements.txt
```

Run the project

```bash
  py main.py
```

## Running unit tests

For unit tests, pyTest and Httpx are used, for the execution of said tests, execute the following command

```bash
  pytest
```

## Technology Stack and Features

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the backend APIRestFull version 0.111.0
    - 🎨 [OpenAPI](https://swagger.io/specification/) for docs.
    - ✅ [SQLite](https://sqlite.org/) for data base.
    - ✅ [pyTest](https://docs.pytest.org/en/7.3.x/) for unite test.
- 🐋 [**Docker Compose**](https://www.docker.com) for development and production.

## Author

- [@AndresOrozcoDev](https://github.com/AndresOrozcoDev)