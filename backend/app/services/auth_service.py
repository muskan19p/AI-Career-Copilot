from backend.app.core.security import hash_password, verify_password, create_access_token
from backend.app.models.user import User
from sqlalchemy.orm import Session

def register_user(db: Session, data):

    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"success": True}

def login_user(db: Session, data):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        return {"success": False}

    if not verify_password(data.password, user.password):
        return {"success": False}

    token = create_access_token({"sub": user.email})

    return {
        "success": True,
        "token": token,
        "user": {
            "name": user.name,
            "email": user.email
        }
    }