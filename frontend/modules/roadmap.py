import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title(
        "🗺 Career Roadmap Generator"
    )

    skill = st.text_input(
        "Enter Skill"
    )

    if st.button(
        "Generate Roadmap"
    ):

        if not skill:

            st.warning(
                "Enter Skill"
            )

            return

        try:

            res = requests.post(
                f"{API}/ai/resume-review",
                json={
                    "text":
                    f"Roadmap for {skill}"
                }
            )

            st.session_state.roadmap_count += 1

            st.session_state.history.append(
                f"Roadmap Generated : {skill}"
            )

            st.subheader(
                "Learning Path"
            )

            roadmap = [
                "Learn Fundamentals",
                "Build Projects",
                "Advanced Concepts",
                "Portfolio Creation",
                "Interview Preparation",
                "Job Applications"
            ]

            for step in roadmap:

                st.success(step)

            st.divider()

            st.subheader(
                "AI Recommendation"
            )

            st.info(
                res.json()["answer"]
            )

        except Exception as e:

            st.error(str(e))