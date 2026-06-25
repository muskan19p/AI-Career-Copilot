from fastapi import APIRouter
from backend.app.services.resume_service import analyze_resume

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):

    result = analyze_resume(
        data["text"]
    )

    return result