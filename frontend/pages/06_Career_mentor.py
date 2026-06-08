import streamlit as st
from utils.api_client import ask_ai

st.header("🤖 Career Mentor")

query = st.text_area(
    "Ask Any Career Question"
)

if st.button("Get Advice"):

    prompt = f"""
    Act as a professional career mentor.

    Question:
    {query}

    Give detailed advice.
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.write(result["response"])
    else:
        st.error(result.get("error"))