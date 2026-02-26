"""HTTP routes for the call attender API."""

from fastapi import APIRouter, Body, HTTPException, Query

from backend.models.call import CallRequest, CallResponse
from backend.services.response_service import CallResponseService

router = APIRouter()
service = CallResponseService()


@router.get("/health")
def healthcheck() -> dict[str, str]:
    """Simple health endpoint for container and uptime probes."""

    return {"status": "ok"}


@router.post("/call", response_model=CallResponse)
def attend_call(
    payload: CallRequest | None = Body(default=None),
    message: str | None = Query(default=None, min_length=1, max_length=500),
) -> CallResponse:
    """Accept a caller message and return generated response and intent.

    Supports both JSON body payloads and the legacy `message` query parameter to
    avoid breaking older clients while migrating integrations.
    """

    resolved_message = payload.message if payload else message
    if resolved_message is None:
        raise HTTPException(status_code=422, detail="A caller message is required.")

    decision = service.generate_response(resolved_message)
    return CallResponse(
        caller_message=resolved_message,
        ai_response=decision.response,
        matched_intent=decision.intent,
    )
