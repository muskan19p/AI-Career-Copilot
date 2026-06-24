import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("📄 Resume Analyzer")

    text = st.text_area("Paste your resume here")

    if st.button("Analyze Resume"):

        res = requests.post(f"{API}/resume/analyze", json={
            "text": text
        })

        data = res.json()

        st.subheader("ATS Score")
        st.metric("Score", data["ats_score"])

        st.subheader("Skills")
        st.write(data["skills"])

        st.subheader("Feedback")
        st.write(data["improvements"])