from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
_memories: list[dict[str, str]] = []


class MemoryRequest(BaseModel):
    content: str
    tag: str = "general"


@router.get("")
def list_memory() -> dict[str, list[dict[str, str]]]:
    return {"memories": _memories}


@router.post("")
def save_memory(payload: MemoryRequest) -> dict[str, str]:
    record = {"id": str(len(_memories) + 1), "content": payload.content, "tag": payload.tag}
    _memories.append(record)
    return record


@router.delete("")
def clear_memory() -> dict[str, str]:
    _memories.clear()
    return {"status": "cleared"}
