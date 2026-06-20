# Residential Services API

A backend service for user authentication and residential leave-request management.

## Why it matters

Residential operations often depend on manual forms and messages. This project demonstrates how login, authorization, and leave workflows can be moved into a structured cloud-ready API.

## What it includes

- User authentication
- Token-based access control
- Leave-request creation and management
- Database models and validation
- Separated routes, services, and security logic

## Technology

Python, FastAPI, SQLAlchemy, JWT authentication, and a relational database.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Configure database and secret values through environment variables before deployment.
