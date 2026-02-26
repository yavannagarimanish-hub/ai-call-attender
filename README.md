# AI Call Attender

An end-to-end starter application for capturing inbound caller details and returning an instant AI-style response.

## What this project does
- Collects complete caller intake details from a web form.
- Sends the intake payload to a FastAPI backend.
- Returns an AI-generated response based on caller message context.
- Marks the request as captured for follow-up.

## End-to-End Flow
1. Caller details are entered in `demo/index.html`.
2. Frontend submits a JSON payload to `POST /call`.
3. Backend validates all required fields with Pydantic.
4. AI response logic generates a contextual reply.
5. Frontend displays request status and AI response.

## Required Intake Fields
The application currently requires all fields below:
- `caller_name`
- `phone_number`
- `email`
- `organization`
- `use_case` (`Hospital`, `College`, `Government Office`, `Startup`, `Other`)
- `preferred_callback_time`
- `message`

## Project Structure
- `backend/main.py` — FastAPI API with field validation and response generation.
- `demo/index.html` — Demo UI to submit complete intake fields.
- `requirements.txt` — Python dependencies.

## Run Locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open the demo page in your browser:
- `demo/index.html`

## API Example
```bash
curl -X POST "http://127.0.0.1:8000/call" \
  -H "Content-Type: application/json" \
  -d '{
    "caller_name":"Jane Doe",
    "phone_number":"+15551234567",
    "email":"jane@company.com",
    "organization":"City General Hospital",
    "use_case":"Hospital",
    "preferred_callback_time":"Tomorrow 2 PM",
    "message":"I need an appointment for next week"
  }'
```

## Status
MVP end-to-end application with complete intake fields.
