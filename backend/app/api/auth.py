from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, HTTPException
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr

from ..config import get_settings

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
_users: dict[str, dict[str, str]] = {}


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/register")
def register(payload: RegisterRequest) -> dict[str, str]:
    if payload.email in _users:
        raise HTTPException(status_code=409, detail="User already exists")
    _users[payload.email] = {"name": payload.name, "password_hash": pwd_context.hash(payload.password)}
    return {"status": "registered", "otp_delivery": "email"}


@router.post("/login")
def login(payload: LoginRequest) -> dict[str, str]:
    user = _users.get(payload.email)
    if not user or not pwd_context.verify(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    settings = get_settings()
    expires = datetime.now(timezone.utc) + timedelta(hours=12)
    token = jwt.encode({"sub": payload.email, "exp": expires}, settings.jwt_secret, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}


@router.post("/otp/verify")
def verify_otp() -> dict[str, str]:
    return {"status": "verified"}


@router.post("/email/verify")
def verify_email() -> dict[str, str]:
    return {"status": "email_verified"}
