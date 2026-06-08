import requests

BASE_URL = "http://127.0.0.1:8000"


def ask_ai(prompt):

    response = requests.post(
        f"{BASE_URL}/generate",
        json={"prompt": prompt}
    )

    return response.json()


def analyze_resume(file):

    files = {
        "file": file
    }

    response = requests.post(
        f"{BASE_URL}/resume-analysis",
        files=files
    )

    return response.json()