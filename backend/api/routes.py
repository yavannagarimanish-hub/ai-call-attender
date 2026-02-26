"""HTTP routes for the call attender API."""

from fastapi import APIRouter

from backend.models.call import CallRequest, CallResponse
from backend.services.response_service import CallResponseService

router = APIRouter()
service = CallResponseService()


@router.get("/health")
def healthcheck() -> dict[str, str]:
    """Simple health endpoint for container and uptime probes."""

    return {"status": "ok"}


@router.post("/call", response_model=CallResponse)
def attend_call(payload: CallRequest) -> CallResponse:
    """Accept a caller message and return generated response and intent."""

    decision = service.generate_response(payload.message)
    return CallResponse(
        caller_message=payload.message,
        ai_response=decision.response,
        matched_intent=decision.intent,
    )
