import streamlit as st
from utils.api_client import ask_ai

st.header("🔗 LinkedIn Optimizer")

headline = st.text_input(
    "Current Headline"
)

about = st.text_area(
    "About Section"
)

if st.button("Optimize Profile"):

    prompt = f"""
    Improve LinkedIn Profile.

    Headline:
    {headline}

    About:
    {about}

    Provide:

    1. Better Headline
    2. Better About Section
    3. SEO Keywords
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.write(result["response"])
    else:
        st.error(result.get("error"))