from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Call Attender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# simple AI logic
def ai_response(message):

    message = message.lower()

    if "appointment" in message:
        return "Your appointment request has been noted."

    if "price" in message:
        return "Our team will share pricing details shortly."

    if "hello" in message:
        return "Hello! How can I assist you today?"

    return "Thank you for calling. Our team will contact you soon."


@app.get("/")
def home():
    return {"AI": "Call Attender Running"}


@app.post("/call")
def attend_call(message: str):

    reply = ai_response(message)

    return {
        "caller_message": message,
        "ai_response": reply
    }
