import streamlit as st
from pages import (
    login,
    dashboard,
    resume,
    chatbot,
    jobs,
    settings,
    history,
    ats,
    roadmap,
    mentor,
    linkedin
)

st.set_page_config(
    page_title="Career OS",
    page_icon="🚀",
    layout="wide"
)

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    login.show()

else:

    st.sidebar.title("🚀 Career OS")

    section = st.sidebar.selectbox(
        "Category",
        [
            "Dashboard",
            "Resume Hub",
            "Interview Hub",
            "Career Center",
            "Account"
        ]
    )

    page = None

    if section == "Dashboard":
        page = "Dashboard"

    elif section == "Resume Hub":
        page = st.sidebar.selectbox(
            "Tools",
            [
                "Resume Builder",
                "ATS Checker",
                "LinkedIn Optimizer"
            ]
        )

    elif section == "Interview Hub":
        page = st.sidebar.selectbox(
            "Tools",
            [
                "AI Chatbot",
                "AI Mentor",
                "Career Roadmap"
            ]
        )

    elif section == "Career Center":
        page = st.sidebar.selectbox(
            "Tools",
            [
                "Jobs",
                "Progress Tracker"
            ]
        )

    elif section == "Account":
        page = st.sidebar.selectbox(
            "Tools",
            [
                "History",
                "Settings"
            ]
        )

    st.sidebar.divider()

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    if page == "Dashboard":
        dashboard.show()

    elif page == "Resume Builder":
        resume.show()

    elif page == "ATS Checker":
        ats.show()

    elif page == "LinkedIn Optimizer":
        linkedin.show()

    elif page == "AI Chatbot":
        chatbot.show()

    elif page == "AI Mentor":
        mentor.show()

    elif page == "Career Roadmap":
        roadmap.show()

    elif page == "Jobs":
        jobs.show()

    elif page == "Progress Tracker":
        dashboard.show()

    elif page == "History":
        history.show()

    elif page == "Settings":
        settings.show()