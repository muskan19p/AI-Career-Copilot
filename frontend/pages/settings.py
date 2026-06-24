import streamlit as st

def show():

    st.title("⚙ Settings")

    st.selectbox("Theme", ["Dark", "Light"])
    st.checkbox("Enable AI Suggestions")
    st.checkbox("Email Notifications")