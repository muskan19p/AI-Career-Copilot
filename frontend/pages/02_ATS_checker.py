import streamlit as st
from utils.api_client import ask_ai

st.header("📊 ATS Score Checker")

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Check ATS Score"):

    prompt = f"""
    Analyze ATS compatibility.

    Job Description:
    {job_description}

    Provide:

    1. ATS Score out of 100
    2. Important Keywords
    3. Missing Skills
    4. Suggestions
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.success("ATS Analysis Complete")
        st.write(result["response"])
    else:
        st.error(result.get("error"))