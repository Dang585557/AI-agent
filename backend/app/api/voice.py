from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SpeakRequest(BaseModel):
    text: str


@router.post("/transcribe")
def transcribe() -> dict[str, str]:
    return {"text": "Transcription placeholder ready for realtime voice."}


@router.post("/speak")
def speak(payload: SpeakRequest) -> dict[str, str]:
    return {"audio_base64": payload.text.encode().hex()}


@router.post("/realtime-token")
def realtime_token() -> dict[str, str]:
    return {"client_secret": "server-generated-realtime-session-token"}
