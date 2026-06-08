import streamlit as st
from utils.api_client import ask_ai

st.header("💼 Job Recommendations")

skills = st.text_area("Enter Your Skills")

education = st.text_input("Education")

if st.button("Get Recommendations"):

    prompt = f"""
    Skills:
    {skills}

    Education:
    {education}

    Suggest:

    1. Best Job Roles
    2. Salary Range
    3. Required Skills
    4. Career Growth
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.write(result["response"])
    else:
        st.error(result.get("error"))