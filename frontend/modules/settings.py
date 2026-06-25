import streamlit as st

def show():

    st.title("⚙ Settings")

    current_theme = st.session_state.get(
        "theme",
        "Dark"
    )

    theme = st.selectbox(
        "Theme",
        ["Dark", "Light"],
        index=0 if current_theme=="Dark" else 1
    )

    st.session_state.theme = theme

    st.divider()

    ai = st.checkbox(
        "Enable AI Suggestions",
        value=True
    )

    email = st.checkbox(
        "Email Notifications",
        value=True
    )

    st.session_state.ai_enabled = ai
    st.session_state.email_enabled = email

    st.success(
        "Settings Updated"
    )