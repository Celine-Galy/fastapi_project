FASTAPI Project
================

This is a simple project to demonstrate how to use FastAPI.

## Installation

```bash
pip install -r requirements.txt
```

## Docker

```bash
docker build -t fastapi-project .
docker run -d --name fastapi_container -p 8000:8000 fastapi-project
docker run -d --name postgres_container -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:latest
docker-compose up -d --build
```

## Usage

```bash
uvicorn main:app --reload
```

## Test

```bash
pytest
```
