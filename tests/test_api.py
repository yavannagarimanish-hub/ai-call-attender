import pytest
from fastapi import HTTPException

from backend.api.routes import attend_call, healthcheck
from backend.main import home
from backend.models.call import CallRequest
from backend.services.response_service import CallResponseService


def test_home_endpoint_returns_service_metadata() -> None:
    data = home()

    assert data["service"] == "AI Call Attender"
    assert data["status"] == "running"


def test_call_route_returns_intent_and_response_from_body() -> None:
    payload = CallRequest(message="hello there")
    response = attend_call(payload=payload)

    assert response.matched_intent == "greeting"
    assert "assist" in response.ai_response.lower()


def test_call_route_supports_legacy_query_parameter() -> None:
    response = attend_call(payload=None, message="Can I know the price?")

    assert response.matched_intent == "pricing_query"


def test_call_route_requires_a_message() -> None:
    with pytest.raises(HTTPException) as exc_info:
        attend_call(payload=None, message=None)

    assert exc_info.value.status_code == 422


def test_response_service_falls_back_to_general_inquiry() -> None:
    service = CallResponseService()
    decision = service.generate_response("Need help with account")

    assert decision.intent == "general_inquiry"


def test_healthcheck() -> None:
    assert healthcheck() == {"status": "ok"}
