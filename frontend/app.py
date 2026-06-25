import streamlit as st

from components.theme import apply_theme

from modules import (
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

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Career OS",
    page_icon="🚀",
    layout="wide"
)

apply_theme()

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "history" not in st.session_state:
    st.session_state.history = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "applied_jobs" not in st.session_state:
    st.session_state.applied_jobs = []

if "ats_count" not in st.session_state:
    st.session_state.ats_count = 0

if "roadmap_count" not in st.session_state:
    st.session_state.roadmap_count = 0

if "user" not in st.session_state:
    st.session_state.user = None

# -----------------------------------
# LOGIN PAGE
# -----------------------------------

if st.session_state.user is None:

    login.show()

# -----------------------------------
# MAIN APP
# -----------------------------------

else:

    st.sidebar.title("🚀 Career OS")

    section = st.sidebar.selectbox(
        "Category",
        [
            "Dashboard",
            "Tools",
            "Career Center",
            "Account"
        ]
    )

    page = None

    # ---------------- DASHBOARD ----------------

    if section == "Dashboard":

        page = "Dashboard"

    # ---------------- TOOLS ----------------

    elif section == "Tools":

        page = st.sidebar.selectbox(
            "Tools",
            [
                "Resume Builder",
                "ATS Checker",
                "LinkedIn Optimizer",
                "AI Chatbot",
                "AI Mentor"
            ]
        )

    # ---------------- CAREER CENTER ----------------

    elif section == "Career Center":

        page = st.sidebar.selectbox(
            "Tools",
            [
                "Jobs",
                "Career Roadmap",
                "Progress Tracker"
            ]
        )

    # ---------------- ACCOUNT ----------------

    elif section == "Account":

        page = st.sidebar.selectbox(
            "Tools",
            [
                "History",
                "Settings"
            ]
        )

    # -----------------------------------
    # USER INFO
    # -----------------------------------

    st.sidebar.divider()

    st.sidebar.success(
         f"Welcome {st.session_state.user['name']}"
    )

    st.sidebar.write(
      st.session_state.user['email']
    ) 

    st.sidebar.divider()

    # -----------------------------------
    # LOGOUT
    # -----------------------------------

    if st.sidebar.button("Logout"):

        st.session_state.user = None

        st.rerun()

    # -----------------------------------
    # ROUTING
    # -----------------------------------

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