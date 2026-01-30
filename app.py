from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

# Hardcoded API key for now (will be shared with evaluators)
API_KEY = "sk_test_123456789"

app = FastAPI()

class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

@app.post("/api/voice-detection")
def voice_detection(
    request: VoiceRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    if request.audioFormat.lower() != "mp3":
        raise HTTPException(
            status_code=400,
            detail="Only mp3 format is supported"
        )
    return {
        "status": "success",
        "language": request.language,
        "classification": "HUMAN",
        "confidenceScore": 0.5,
        "explanation": "Temporary response"
    }

