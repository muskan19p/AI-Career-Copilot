from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from backend.resume_parser import extract_text
from backend.ai_service import ask_openai
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

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

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input.prompt
        )

        return {
            "success": True,
            "response": response.output_text
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
        Analyze this resume.

        Resume:

        {resume_text}

        Give:

        1. Strengths
        2. Weaknesses
        3. Missing Skills
        4. Hiring Chances
        5. Improvement Suggestions
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
        