import streamlit as st

def sidebar(user):

    st.sidebar.title("Career OS 🚀")

    page = st.sidebar.radio("Navigation", [
        "Dashboard",
        "Resume",
        "Jobs",
        "AI Coach",
        "Recruiter",
        "History",
        "Settings"
    ])

    st.sidebar.write(f"Logged in as {user['name']}")

    logout = st.sidebar.button("Logout")

    return page, logout