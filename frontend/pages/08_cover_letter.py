import streamlit as st
from utils.api_client import ask_ai

st.header("✉️ Cover Letter Generator")

company = st.text_input(
    "Company Name"
)

role = st.text_input(
    "Job Role"
)

skills = st.text_area(
    "Your Skills"
)

if st.button("Generate Cover Letter"):

    prompt = f"""
    Generate a professional cover letter.

    Company:
    {company}

    Role:
    {role}

    Skills:
    {skills}
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.write(result["response"])
    else:
        st.error(result.get("error"))