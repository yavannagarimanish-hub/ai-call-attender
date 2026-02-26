from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="AI Call Attender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class CallRequest(BaseModel):
    caller_name: str = Field(..., min_length=2, max_length=80)
    phone_number: str = Field(..., min_length=7, max_length=20)
    email: str = Field(..., min_length=5, max_length=120)
    organization: str = Field(..., min_length=2, max_length=120)
    use_case: Literal["Hospital", "College", "Government Office", "Startup", "Other"]
    preferred_callback_time: str = Field(..., min_length=2, max_length=60)
    message: str = Field(..., min_length=3, max_length=500)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("email must be a valid address")
        return value


# simple AI logic

def ai_response(message: str, use_case: str) -> str:
    message_lower = message.lower()

    if "appointment" in message_lower:
        return "Your appointment request has been noted and will be forwarded to the scheduling desk."

    if "price" in message_lower or "cost" in message_lower:
        return "Thanks for asking about pricing. Our team will share detailed plans shortly."

    if "hello" in message_lower or "hi" in message_lower:
        return f"Hello! Thanks for contacting us regarding your {use_case.lower()} workflow. How can I assist further?"

    return "Thank you for the details. Our team will review your request and contact you soon."


@app.get("/")
def home() -> dict[str, str]:
    return {"AI": "Call Attender Running"}


@app.post("/call")
def attend_call(payload: CallRequest) -> dict[str, str]:
    reply = ai_response(payload.message, payload.use_case)

    return {
        "caller_name": payload.caller_name,
        "phone_number": payload.phone_number,
        "email": payload.email,
        "organization": payload.organization,
        "use_case": payload.use_case,
        "preferred_callback_time": payload.preferred_callback_time,
        "caller_message": payload.message,
        "ai_response": reply,
        "status": "captured",
    }
