import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("📊 ATS Score Checker")

    job_desc = st.text_area("Job Description")
    resume = st.text_area("Resume Text")

    if st.button("Check ATS Score"):

        res = requests.post(f"{API}/resume/analyze", json={
            "text": resume
        })

        data = res.json()

        score = data["ats_score"]

        st.metric("ATS Score", score)

        if score < 70:
            st.error("Low ATS match - improve keywords")
        else:
            st.success("Good match for job")