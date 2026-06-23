from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.database import SessionLocal, engine, Base
from backend import models

from backend.schemas import UserCreate, UserLogin
from backend.crud import create_user, authenticate_user
from backend.ai_service import ask_ai


print("🔥 MAIN.PY LOADED")


Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- REGISTER ----------------
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = create_user(
        db,
        name=user.name,
        email=user.email,
        password=user.password
    )

    return {
        "success": True,
        "user_id": db_user.id,
        "message": "User created"
    }


# ---------------- LOGIN ----------------
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = authenticate_user(
        db,
        email=user.email,
        password=user.password
    )

    if not db_user:
        return {
            "success": False,
            "message": "User not found or wrong password"
        }

    return {
        "success": True,
        "user_id": db_user.id,
        "name": db_user.name
    }


# ---------------- AI ----------------
@app.post("/generate")
def generate(prompt: str):

    return {
        "success": True,
        "response": ask_ai(prompt)
    }
    
@app.get("/")
def home():
    return {
        "message": "Career OS Backend is running 🚀"
    }