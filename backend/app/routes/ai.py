from fastapi import APIRouter
from backend.app.services.ai_service import resume_review

router = APIRouter()

@router.post("/resume-review")
def review(data: dict):
    return resume_review(data["text"])