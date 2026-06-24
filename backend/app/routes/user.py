from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.user import User

router = APIRouter()

@router.get("/me")
def get_user(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {"success": False}

    return {
        "success": True,
        "user": {
            "name": user.name,
            "email": user.email
        }
    }