import streamlit as st

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


# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ================= STATE INIT ================= #

if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"

if "theme" not in st.session_state:
    st.session_state.theme = "☀️ Light"
    
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ================= THEME SIDEBAR ================= #

st.sidebar.markdown("## 🚀 AI Career Copilot")
st.sidebar.caption("AI-powered Career Assistant")

theme = st.sidebar.selectbox(
    "🎨 Theme",
    ["☀️ Light", "🌙 Dark", "🖥️ System"],
    index=0
)


st.sidebar.markdown("---")


# ================= NAVIGATION ================= #

PAGES = [

    "🏠 Dashboard",

    "📄 Resume Analyzer",
    "🎯 ATS Checker",
    "💼 Job Recommendations",
    "🎤 Interview Prep",
    "🗺️ Study Roadmap",
    "🧠 Career Mentor",
    "🤖 AI Chatbot",
    "✉️ Cover Letter",
    "🔗 LinkedIn Optimizer",

    "📚 History"
]

current_index = (
    PAGES.index(st.session_state.page)
    if st.session_state.page in PAGES
    else 0
)

selected_page = st.sidebar.selectbox(
    "📍 Navigate",
    PAGES,
    index=current_index
)

if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    

if st.session_state.logged_in:

    st.sidebar.success(
        f"👤 {st.session_state.username}"
    )

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False

        st.session_state.user_id = None

        st.session_state.username = ""

        st.rerun()
        
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "user_id" not in st.session_state:
    st.session_state.user_id = None
    
    
# ================= THEME SYSTEM ================= #

if theme == "☀️ Light":

    st.markdown("""
    <style>
    .main {
        background: #f8fafc;
        color: #111827;
    }

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    .stButton>button {
        background: #2563eb;
        color: white;
        border-radius: 10px;
    }
    
    .stApp{
    background:#f8fafc;
}

div[data-testid="metric-container"]{
    background:white;
    border:1px solid #e5e7eb;
    border-radius:15px;
    padding:15px;
}

.stButton > button{
    width:100%;
    border:none;
    border-radius:12px;
    font-weight:600;
    height:48px;
}

    </style>
    """, unsafe_allow_html=True)


elif theme == "🌙 Dark":

    st.markdown("""
    <style>
    .main {
        background: #0b1220;
        color: white;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a, #111827);
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    .stButton>button {
        background: linear-gradient(135deg,#2563eb,#7c3aed);
        color: white;
        border-radius: 10px;
        border: none;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 4px 20px rgba(99,102,241,0.4);
    }

    </style>
    """, unsafe_allow_html=True)


elif theme == "🖥️ System":

    st.markdown("""
    <style>
    .main {
        background: #111827;
        color: white;
    }

    [data-testid="stSidebar"] {
        background: #1f2937;
    }

    </style>
    """, unsafe_allow_html=True)


# ================= ROUTING ================= #

page = st.session_state.page


if page == "🔐 Login":
    show_login()

elif page == "📝 Register":
    show_register()

elif page == "📚 History":

    if st.session_state.logged_in:
        show_history()
    else:
        st.warning("Please Login First")
        
if page == "🏠 Dashboard":

    # Header
    top1, top2, top3 = st.columns([6, 1, 1])

    with top1:
        st.markdown("## 🚀 AI Career Copilot Dashboard")
        st.write("Your complete AI-powered career control center")

    if not st.session_state.logged_in:

        with top2:
            if st.button("🔐 Login"):
                st.session_state.page = "🔐 Login"
                st.rerun()

        with top3:
            if st.button("📝 Sign Up"):
                st.session_state.page = "📝 Register"
                st.rerun()

    else:

        with top2:
            st.write(f"👋 {st.session_state.username}")

        with top3:
            if st.button("🚪 Logout"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.session_state.user_id = None
                st.rerun()

    st.markdown("---")

    # Feature Cards
    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("📄 Resume Analyzer", use_container_width=True):
            st.session_state.page = "📄 Resume Analyzer"
            st.rerun()

        if st.button("🎯 ATS Checker", use_container_width=True):
            st.session_state.page = "🎯 ATS Checker"
            st.rerun()

    with col2:

        if st.button("💼 Job Recommendations", use_container_width=True):
            st.session_state.page = "💼 Job Recommendations"
            st.rerun()

        if st.button("🎤 Interview Prep", use_container_width=True):
            st.session_state.page = "🎤 Interview Prep"
            st.rerun()

    with col3:

        if st.button("🗺️ Study Roadmap", use_container_width=True):
            st.session_state.page = "🗺️ Study Roadmap"
            st.rerun()

        if st.button("🤖 AI Chatbot", use_container_width=True):
            st.session_state.page = "🤖 AI Chatbot"
            st.rerun()

    st.markdown("---")

    st.markdown("### ⚡ System Status")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("AI Modules", "9+")
    c2.metric("Tools", "Career Suite")
    c3.metric("Performance", "High")
    c4.metric("Status", "Active 🚀")
        


elif page == "📄 Resume Analyzer":

    if st.session_state.logged_in:
        show_resume()
    else:
        st.warning("Please Login First")

elif page == "🎯 ATS Checker":
    
    if st.session_state.logged_in:
        show_ats()
    else:
        st.warning("Please Login First")

elif page == "💼 Job Recommendations":
    
    if st.session_state.logged_in:
        show_jobs()
    else:
        st.warning("Please Login First")

elif page == "🎤 Interview Prep":
    
    if st.session_state.logged_in:
        show_interview()
    else:
        st.warning("Please Login First")

elif page == "🗺️ Study Roadmap":
    
    
    show_roadmap()
    

elif page == "🧠 Career Mentor":
    
    
    show_mentor()
    

elif page == "🤖 AI Chatbot":
    
    show_chatbot()
    

elif page == "✉️ Cover Letter":
    
    if st.session_state.logged_in:
        show_cover_letter()
    else:
        st.warning("Please Login First")

elif page == "🔗 LinkedIn Optimizer":
    
    if st.session_state.logged_in:
        show_linkedin()
    else:
        st.warning("Please Login First")
    