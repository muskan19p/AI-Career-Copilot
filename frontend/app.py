import streamlit as st

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Copilot")
st.caption("Your Personal AI-Powered Career Assistant")

st.markdown("---")

st.markdown(
    """
    ### Welcome 👋

    Analyze resumes, improve ATS scores, generate study roadmaps,
    prepare for interviews, optimize LinkedIn profiles and get AI career guidance.
    """
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("📄 Resume Analysis")
    st.write("AI-powered resume review")

    st.info("📊 ATS Score Checking")
    st.write("Resume ATS compatibility")

    st.info("💼 Job Recommendations")
    st.write("Roles based on skills")

with col2:

    st.info("🎤 Interview Preparation")
    st.write("Technical + HR Questions")

    st.info("📚 Study Roadmaps")
    st.write("Goal-based learning plans")

    st.info("🤖 Career Guidance")
    st.write("Personal AI mentor")

with col3:

    st.info("✉️ Cover Letters")
    st.write("Generate professional cover letters")

    st.info("🔗 LinkedIn Optimization")
    st.write("Improve profile visibility")

    st.info("🚀 Future Features")
    st.write("Dashboard, History, Analytics")

st.markdown("---")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric("AI Features", "8")
metric2.metric("Resume Tools", "2")
metric3.metric("Career Tools", "4")
metric4.metric("Status", "Active")

st.markdown("---")

st.success(
    "Select any feature from the left sidebar to get started."
)