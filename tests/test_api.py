from backend.api.routes import attend_call, healthcheck
from backend.main import home
from backend.models.call import CallRequest
from backend.services.response_service import CallResponseService


def test_home_endpoint_returns_service_metadata() -> None:
    data = home()

    assert data["service"] == "AI Call Attender"
    assert data["status"] == "running"


def test_call_route_returns_intent_and_response() -> None:
    payload = CallRequest(message="hello there")
    response = attend_call(payload)

    assert response.matched_intent == "greeting"
    assert "assist" in response.ai_response.lower()


def test_response_service_falls_back_to_general_inquiry() -> None:
    service = CallResponseService()
    decision = service.generate_response("Need help with account")

    assert decision.intent == "general_inquiry"


def test_healthcheck() -> None:
    assert healthcheck() == {"status": "ok"}
