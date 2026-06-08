import requests

BASE_URL = "http://127.0.0.1:8000"

def ask_ai(prompt):

    try:

        response = requests.post(
            f"{BASE_URL}/generate",
            json={
                "prompt": prompt
            }
        )

        return response.json()

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

def analyze_resume(file):

    try:

        files = {
            "file": file
        }

        response = requests.post(
            f"{BASE_URL}/resume-analysis",
            files=files
        )

        return response.json()

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }