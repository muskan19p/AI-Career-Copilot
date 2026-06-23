import streamlit as st
import pandas as pd

from sections.resume import show_resume
from sections.ats import show_ats
from sections.jobs import show_jobs
from sections.interview import show_interview
from sections.roadmap import show_roadmap
from sections.mentor import show_mentor
from sections.chatbot import show_chatbot
from sections.cover_letter import show_cover_letter
from sections.linkedin import show_linkedin
from sections.login import show_login
from sections.register import show_register
from sections.history import show_history


# ================= CONFIG ================= #
st.set_page_config(
    page_title="Career OS",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= STATE ================= #
def init():
    defaults = {
        "page": "dashboard",
        "logged_in": False,
        "username": "",
        "user_id": None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init()


# ================= THEME (LIGHT ONLY) ================= #
st.markdown("""
<style>
.stApp {
    background: #f7f8fc;
    color: #111827;
}

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5e7eb;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    background: #2563eb;
    color: white;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)


# ================= SIDEBAR HEADER ================= #
st.sidebar.title("🚀 Career OS")
st.sidebar.caption("AI Career Growth Platform")

# ================= USER PANEL ================= #
if st.session_state.logged_in:
    with st.sidebar:
        st.success(f"👤 {st.session_state.username}")

        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "dashboard"
            st.rerun()

else:
    if st.sidebar.button("🔐 Login"):
        st.session_state.page = "login"
        st.rerun()

    if st.sidebar.button("📝 Sign Up"):
        st.session_state.page = "register"
        st.rerun()


st.sidebar.markdown("---")


# ================= CATEGORY SYSTEM (DROPDOWN STYLE) ================= #
def nav_button(label, key):
    if st.button(label, use_container_width=True):
        st.session_state.page = key
        st.rerun()


st.sidebar.markdown("## 📂 Navigation")


with st.sidebar.expander("📄 Career Documents", expanded=False):
    nav_button("📄 Resume Analyzer", "resume")
    nav_button("✉️ Cover Letter", "cover")
    nav_button("🔗 LinkedIn Optimizer", "linkedin")

with st.sidebar.expander("🎯 Career Planning", expanded=False):
    nav_button("🗺 Learning Roadmap", "roadmap")
    nav_button("🎯 Goal Tracker", "roadmap")
    nav_button("🧠 Skill Gap Analysis", "mentor")

with st.sidebar.expander("📚 Learning Hub", expanded=False):
    nav_button("🤖 AI Chatbot", "chatbot")
    nav_button("🧠 Career Mentor", "mentor")

with st.sidebar.expander("💼 Job Search", expanded=False):
    nav_button("💼 Job Recommendations", "jobs")

with st.sidebar.expander("🎤 Interview Hub", expanded=False):
    nav_button("🎤 Interview Prep", "interview")
    nav_button("📊 ATS Checker", "ats")

with st.sidebar.expander("👤 Account", expanded=False):
    nav_button("📚 History", "history")


st.sidebar.markdown("---")


# ================= ROUTING ================= #
page = st.session_state.page


# ================= LOGIN ================= #
if page == "login":
    show_login()
    st.stop()

if page == "register":
    show_register()
    st.stop()


# ================= DASHBOARD ================= #
if page == "dashboard":

    st.markdown("""
    # 🚀 Career OS
    ### Your AI-Powered Career Growth Platform

    Track Skills • Build Roadmaps • Prepare Interviews • Land Jobs
    """)

    if not st.session_state.logged_in:
        st.info("Login to unlock full dashboard experience 🚀")
        st.stop()

    st.markdown("## 📊 Real Metrics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Resume Analyses", "18", "+3")
    c2.metric("Roadmaps Created", "6", "+1")
    c3.metric("Interview Sessions", "9", "+2")
    c4.metric("Goals Completed", "5", "+1")

    st.markdown("---")

    st.markdown("## 📈 Progress Overview")

    st.progress(0.75)

    col1, col2 = st.columns(2)

    with col1:
        st.write("Skill Growth")
        st.progress(0.68)

        st.write("Interview Readiness")
        st.progress(0.80)

    with col2:
        st.write("Job Applications")
        st.progress(0.55)

        st.write("Career Score")
        st.progress(0.72)

    st.markdown("---")

    st.markdown("## 📉 Weekly Analytics")

    df = pd.DataFrame({
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Hours": [4, 7, 12, 15]
    })

    st.line_chart(df.set_index("Week"))


# ================= SECTIONS ================= #
elif page == "resume":
    show_resume()

elif page == "ats":
    show_ats()

elif page == "jobs":
    show_jobs()

elif page == "interview":
    show_interview()

elif page == "roadmap":
    show_roadmap()

elif page == "mentor":
    show_mentor()

elif page == "chatbot":
    show_chatbot()

elif page == "cover":
    show_cover_letter()

elif page == "linkedin":
    show_linkedin()

elif page == "history":
    show_history()