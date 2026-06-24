from fastapi import APIRouter

router = APIRouter()

@router.get("/candidates")
def candidates():
    return {
        "candidates": [
            {"name": "Amit", "score": 85},
            {"name": "Sara", "score": 78},
            {"name": "John", "score": 90}
        ]
    }