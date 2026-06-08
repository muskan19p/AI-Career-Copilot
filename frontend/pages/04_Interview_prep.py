import streamlit as st
from utils.api_client import ask_ai

st.header("🎤 Interview Preparation")

role = st.text_input("Job Role")

level = st.selectbox(
    "Experience Level",
    ["Fresher", "Intern", "1-2 Years", "3+ Years"]
)

if st.button("Generate Questions"):

    prompt = f"""
    Generate interview questions for:

    Role: {role}
    Level: {level}

    Include:

    Technical Questions
    HR Questions
    Scenario Based Questions

    Also provide answers.
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.write(result["response"])
    else:
        st.error(result.get("error"))