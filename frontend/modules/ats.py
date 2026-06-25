import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("📊 ATS Score Checker")

    job_desc = st.text_area(
        "Job Description"
    )

    resume = st.text_area(
        "Resume Text"
    )

    if st.button(
        "Check ATS Score"
    ):

        if not resume:

            st.warning(
                "Enter Resume Text"
            )

            return

        try:

            res = requests.post(
                f"{API}/resume/analyze",
                json={
                    "text": resume
                }
            )

            data = res.json()

            score = data["ats_score"]

            st.metric(
                "ATS Score",
                score
            )

            if score < 70:

                st.error(
                    "Low ATS Match"
                )

            else:

                st.success(
                    "Good ATS Match"
                )

            st.session_state.ats_count += 1

            st.session_state.history.append(
                f"ATS Checked : {score}%"
            )

        except Exception as e:

            st.error(str(e))