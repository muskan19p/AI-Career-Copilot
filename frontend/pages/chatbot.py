import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("🤖 AI Career Chatbot")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    prompt = st.text_input("Ask Career Question")

    if st.button("Send"):

        res = requests.post(f"{API}/ai/resume-review", json={
            "text": prompt
        })

        answer = res.json()["answer"]

        st.session_state.chat.append((prompt, answer))

    for q, a in st.session_state.chat:
        st.write("🧑 You:", q)
        st.write("🤖 AI:", a)