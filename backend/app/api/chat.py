from fastapi import APIRouter
from pydantic import BaseModel

from ..core.agent.orchestrator import AgentOrchestrator

router = APIRouter()
orchestrator = AgentOrchestrator()
_history: list[dict[str, str]] = []


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


@router.post("/message")
async def message(payload: ChatRequest) -> dict[str, str]:
    answer = await orchestrator.respond(payload.message, payload.session_id)
    _history.extend([
        {"role": "user", "content": payload.message},
        {"role": "assistant", "content": answer},
    ])
    return {"response": answer, "session_id": payload.session_id}


@router.get("/history")
def history() -> dict[str, list[dict[str, str]]]:
    return {"messages": _history}
