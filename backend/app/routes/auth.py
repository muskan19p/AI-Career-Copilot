from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.services.auth_service import register_user, login_user

from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(data: dict):
    return {
        "success": True,
        "user": {
            "name": "Demo User",
            "email": data["email"]
        }
    }

@router.post("/register")
def register(data: dict):
    return {"success": True}