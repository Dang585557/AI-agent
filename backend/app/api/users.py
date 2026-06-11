from fastapi import APIRouter

router = APIRouter()


@router.get("/me")
def me() -> dict[str, str]:
    return {"name": "Dang User", "plan": "pro", "locale": "th"}
