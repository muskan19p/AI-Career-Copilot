import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("🗺 Career Roadmap Generator")

    skill = st.text_input("Enter Skill (e.g. AI, Web Dev)")

    if st.button("Generate Roadmap"):

        res = requests.post(f"{API}/ai/resume-review", json={
            "text": f"Give roadmap for {skill}"
        })

        st.json({
            "roadmap": [
                "Basics",
                "Intermediate Projects",
                "Advanced Projects",
                "Job Preparation"
            ],
            "ai_response": res.json()["answer"]
        })