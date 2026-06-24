from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def jobs():
    return {
        "jobs": [
            {"title": "AI Engineer", "company": "Google"},
            {"title": "Backend Dev", "company": "Microsoft"}
        ]
    }