# AI Call Attender

Production-oriented FastAPI service for handling inbound caller messages with lightweight intent detection and deterministic, business-safe responses.

## Why this project
Many organizations miss inbound opportunities due to delayed or inconsistent call handling. This service provides a clean foundation for:
- classifying common caller intents,
- returning reliable responses quickly,
- integrating downstream workflows (CRM ticketing, appointment systems, analytics).

## Features
- **Structured API contracts** using Pydantic request/response models.
- **Service-layer architecture** for clean separation of transport and domain logic.
- **Input validation** (required message, bounded length).
- **Operational endpoints** (`/` metadata, `/health` liveness).
- **Environment-aware configuration** (app metadata + CORS).
- **Automated tests** for core API behavior.

## Project structure

```text
backend/
  api/                # HTTP routes
  core/               # Configuration and shared infrastructure concerns
  models/             # API contracts
  services/           # Domain/business logic
  main.py             # FastAPI app composition

demo/                 # Optional local static demo UI

tests/                # API tests
```

## Quickstart

### 1) Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run the API
```bash
uvicorn backend.main:app --reload
```

API docs:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### 3) Try the API
```bash
curl -X POST "http://127.0.0.1:8000/call" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, I need appointment details"}'
```

Example response:
```json
{
  "caller_message": "Hello, I need appointment details",
  "ai_response": "Your appointment request has been noted. Our team will follow up shortly.",
  "matched_intent": "appointment_request"
}
```

## Configuration
Set these environment variables as needed:

- `APP_NAME` (default: `AI Call Attender`)
- `APP_VERSION` (default: `1.0.0`)
- `APP_ENV` (default: `development`)
- `CORS_ALLOW_ORIGINS` (comma-separated, default: `*`)

Example:
```bash
export APP_ENV=production
export CORS_ALLOW_ORIGINS="https://your-frontend.example.com"
```

## Testing
```bash
pytest -q
```

## Security and production notes
- Restrict CORS origins in production.
- Place behind a reverse proxy/API gateway with rate limiting and request logging.
- Extend `CallResponseService` with robust NLP/LLM intent parsing and fallback guardrails.
- Add authentication/authorization before exposing non-public endpoints.

## Roadmap suggestions
- Add persistence for call logs and intent analytics.
- Add async integration adapters (CRM, SMS, email callbacks).
- Add observability stack (structured logs, metrics, tracing).
- Add CI pipeline for tests, linting, and vulnerability scanning.
