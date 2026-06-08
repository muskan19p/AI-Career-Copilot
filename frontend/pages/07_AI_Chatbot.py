import streamlit as st
from utils.api_client import ask_ai

st.header("💬 AI Career Chatbot")

question = st.chat_input(
    "Ask Anything..."
)

if question:

    prompt = f"""
    Answer the following question:

    {question}
    """

    result = ask_ai(prompt)

    if result.get("success"):
        st.chat_message("user").write(question)
        st.chat_message("assistant").write(
            result["response"]
        )