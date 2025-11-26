# Weather API Backend

FastAPI-based backend service that wraps the Open-Meteo API for weather data retrieval.

## Features

- RESTful API with automatic OpenAPI documentation
- Async/await for performance
- In-memory caching with TTL
- Type-safe data validation with Pydantic
- Clean architecture with service layer pattern
- CORS support for frontend integration
- Health check endpoint

## Installation

### Using Poetry

```bash
# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -
```

# Install dependencies
```bash
poetry install
```

# Activate virtual environment
```bash
poetry shell
```

## Running

### With Poetry

```bash
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Without Poetry

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Development Tools

Poetry provides additional development tools:

```bash
# Format code with Black
poetry run black .
```

```bash
# Lint code with Ruff
poetry run ruff check .
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

Configure in `app/core/config.py`:
- `CORS_ORIGINS`: List of allowed origins for CORS
- `CACHE_TTL_SECONDS`: Cache time-to-live (default: 300 seconds)

## Architecture

```
backend/
├── main.py                 # FastAPI application entry point
├── pyproject.toml          # Poetry configuration
├── poetry.lock             # Locked dependencies
├── app/
│   ├── api/
│   │   └── routes.py      # API route handlers
│   ├── core/
│   │   └── config.py      # Configuration management
│   ├── schemas/
│   │   └── weather.py     # Pydantic models
│   └── services/
│       ├── weather_service.py  # Business logic
│       └── cache_service.py    # Caching implementation
```
