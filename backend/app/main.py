from fastapi import FastAPI
from backend.app.core.database import Base, engine

from backend.app.routes import auth, user, ai, resume, jobs, dashboard, recruiter

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Career OS SaaS")

app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user")
app.include_router(ai.router, prefix="/ai")
app.include_router(resume.router, prefix="/resume")
app.include_router(jobs.router, prefix="/jobs")
app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(recruiter.router, prefix="/recruiter")

@app.get("/")
def root():
    return {"status": "Career OS Running 🚀"}