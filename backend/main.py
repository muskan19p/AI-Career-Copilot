from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from backend.resume_parser import extract_text
from backend.ai_service import ask_openai

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
    file: UploadFile = File(...)
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

        return {
            "success": True,
            "analysis": analysis
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
        