import streamlit as st
from utils.api_client import ask_ai


def show_chatbot():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#06b6d4,#2563eb);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>💬 AI Career Chatbot</h1>
        <p>
        Ask career questions, resume queries, interview doubts,
        skill recommendations, learning paths, or job guidance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input(
        "Ask your career question..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        prompt = f"""
You are an expert AI Career Assistant.

Answer professionally.

Question:
{question}
"""

        with st.spinner("Thinking..."):

            result = ask_ai(prompt)

        if result.get("success"):

            response = result["response"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            with st.chat_message("assistant"):
                st.markdown(response)

        else:

            error_msg = result.get(
                "error",
                "Unable to generate response"
            )

            with st.chat_message("assistant"):
                st.error(error_msg)