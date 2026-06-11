from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
def summary() -> dict[str, object]:
    return {
        "active_sessions": 8,
        "messages": 42,
        "voice_minutes": 16,
        "images_generated": 7,
        "top_intents": ["planning", "writing", "image_generation"],
    }
