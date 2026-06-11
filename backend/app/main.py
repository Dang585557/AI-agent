from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import analytics, auth, chat, images, memory, notifications, users, voice
from .config import get_settings
from .startup import startup

settings = get_settings()
app = FastAPI(title="DANG-AI-AGENT API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", startup)
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["chat"])
app.include_router(voice.router, prefix="/api/v1/voice", tags=["voice"])
app.include_router(images.router, prefix="/api/v1/images", tags=["images"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(memory.router, prefix="/api/v1/memory", tags=["memory"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
app.include_router(notifications.router, prefix="/api/v1/notifications", tags=["notifications"])


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "dang-ai-agent"}
