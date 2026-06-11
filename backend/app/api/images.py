from fastapi import APIRouter
from pydantic import BaseModel

from ..core.llm.image_model import ImageModel

router = APIRouter()
_images: list[dict[str, str]] = []


class ImageRequest(BaseModel):
    prompt: str
    size: str = "1024x1024"


@router.post("/generate")
async def generate(payload: ImageRequest) -> dict[str, str]:
    url = await ImageModel().generate(payload.prompt, payload.size)
    record = {"prompt": payload.prompt, "url": url}
    _images.append(record)
    return record


@router.get("")
def list_images() -> dict[str, list[dict[str, str]]]:
    return {"images": _images}
