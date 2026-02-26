"""Domain service for generating AI call responses."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResponseDecision:
    """Result of processing a caller message."""

    intent: str
    response: str


class CallResponseService:
    """Encapsulates response selection logic for incoming messages."""

    _intent_map: tuple[tuple[str, ResponseDecision], ...] = (
        (
            "appointment",
            ResponseDecision(
                intent="appointment_request",
                response="Your appointment request has been noted. Our team will follow up shortly.",
            ),
        ),
        (
            "price",
            ResponseDecision(
                intent="pricing_query",
                response="Thanks for your interest. We will share pricing details shortly.",
            ),
        ),
        (
            "hello",
            ResponseDecision(
                intent="greeting",
                response="Hello! How can I assist you today?",
            ),
        ),
    )

    _default_decision = ResponseDecision(
        intent="general_inquiry",
        response="Thank you for calling. Our team will contact you soon.",
    )

    def generate_response(self, message: str) -> ResponseDecision:
        """Generate a response decision for a caller message."""

        lowered_message = message.lower()

        for keyword, decision in self._intent_map:
            if keyword in lowered_message:
                return decision

        return self._default_decision
