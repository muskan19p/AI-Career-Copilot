from fastapi import APIRouter

router = APIRouter()

applied_jobs = []

@router.post("/apply")
def apply_job(data: dict):

    applied_jobs.append(data)

    return {
        "success": True,
        "message": "Application Submitted Successfully"
    }


@router.get("/history")
def history():

    return applied_jobs