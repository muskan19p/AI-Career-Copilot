from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from backend.resume_parser import extract_text
from backend.ai_service import ask_openai
from sqlalchemy.orm import Session
from fastapi import Depends
from backend.crud import get_user_history, save_resume_analysis
from backend.crud import delete_history
from backend.schemas import (
    UserCreate,
    UserLogin
)

from backend.crud import (
    create_user,
    get_user_by_email
)

from backend.auth import verify_password

from backend.database import (
    Base,
    engine,
    get_db
)

from backend.schemas import UserCreate
from backend.crud import create_user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Career Copilot",
    version="1.0"
)

class UserPrompt(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {
        "message": "AI Career Copilot Running",
        "status": "Running"
    }

@app.post("/generate")
def generate(user_input: UserPrompt):

    try:

        response = ask_openai(
            user_input.prompt
        )

        return {
            "success": True,
            "response": response
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

@app.post("/resume-analysis")
async def resume_analysis(
    user_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    try:

        resume_text = extract_text(file)

        prompt = f"""
        Analyze this resume carefully.

        Resume:

        {resume_text}

        Provide:

        1. Strengths
        2. Weaknesses
        3. Missing Skills
        4. ATS Score
        5. Hiring Chances
        6. Suggestions
        """

        analysis = ask_openai(prompt)

        # Save to database
        save_resume_analysis(
            db,
            user_id,
            resume_text,
            analysis
        )

        return {
            "success": True,
            "analysis": analysis
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
        
@app.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(
        db,
        user.name,
        user.email,
        user.password
    )
    
    
@app.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if not existing_user:

        return {
            "success": False,
            "message": "User not found"
        }

    if not verify_password(
        user.password,
        existing_user.password
    ):

        return {
            "success": False,
            "message": "Wrong password"
        }

    return {
        "success": True,
        "message": "Login successful",
        "user_id": existing_user.id,
        "name": existing_user.name
    }
    
@app.get("/history/{user_id}")
def history(
        user_id: int,
        db: Session = Depends(get_db)
):

    data = get_user_history(
        db,
        user_id
    )

    return {
        "success": True,
        "history": data
    }
    
 
@app.delete("/history/{history_id}")
def remove_history(
        history_id: int,
        db: Session = Depends(get_db)
):

    deleted = delete_history(
        db,
        history_id
    )

    return {
        "success": deleted
    }   