from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def dashboard():

    return {
        "metrics": {
            "jobs_applied": 15,
            "resume_score": 82,
            "interviews": 4
        },
        "analytics": [
            {"month": "Jan", "score": 60},
            {"month": "Feb", "score": 65},
            {"month": "Mar", "score": 70},
            {"month": "Apr", "score": 75},
            {"month": "May", "score": 82}
        ]
    }