import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("🧠 AI Mentor")

    goal = st.text_input("Your Career Goal")

    if st.button("Get Mentor Plan"):

        res = requests.post(f"{API}/ai/resume-review", json={
            "text": f"Create career roadmap for {goal}"
        })

        st.success(res.json()["answer"])