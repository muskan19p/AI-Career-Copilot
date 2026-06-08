import streamlit as st
from utils.api_client import ask_ai

st.header("📚 Study Roadmap")

goal = st.text_input(
    "Enter Career Goal"
)

duration = st.selectbox(
    "Duration",
    ["1 Month", "3 Months", "6 Months", "1 Year"]
)

if st.button("Generate Roadmap"):

    prompt = f"""
    Create a roadmap.

    Goal:
    {goal}

    Duration:
    {duration}

    Include:

    Weekly Plan
    Skills
    Projects
    Resources
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.write(result["response"])
    else:
        st.error(result.get("error"))