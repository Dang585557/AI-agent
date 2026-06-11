from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
_notifications = [{"id": "1", "title": "Daily briefing is ready", "read": "false"}]


class NotificationRequest(BaseModel):
    title: str


@router.get("")
def list_notifications() -> dict[str, list[dict[str, str]]]:
    return {"notifications": _notifications}


@router.post("")
def create_notification(payload: NotificationRequest) -> dict[str, str]:
    item = {"id": str(len(_notifications) + 1), "title": payload.title, "read": "false"}
    _notifications.append(item)
    return item


@router.patch("/{notification_id}")
def mark_read(notification_id: str) -> dict[str, str]:
    return {"id": notification_id, "read": "true"}
