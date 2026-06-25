import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("🤖 AI Career Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    prompt = st.chat_input(
        "Ask anything about career, jobs, resume..."
    )

    if prompt:

        try:

            res = requests.post(
                f"{API}/ai/resume-review",
                json={
                    "text": prompt
                }
            )

            answer = res.json()["answer"]

            st.session_state.chat_history.append(
                {
                    "question": prompt,
                    "answer": answer
                }
            )

            st.session_state.history.append(
                f"AI Chat : {prompt}"
            )

        except Exception as e:

            st.error(str(e))

    for chat in st.session_state.chat_history:

        with st.chat_message("user"):
            st.write(chat["question"])

        with st.chat_message("assistant"):
            st.write(chat["answer"])

    if st.button("🗑 Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()