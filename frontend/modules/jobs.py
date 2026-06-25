import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("💼 Job Recommendations")

    jobs = [

        {
            "title":"Python Developer",
            "location":"Remote",
            "level":"Entry Level"
        },

        {
            "title":"Backend Developer",
            "location":"Remote",
            "level":"Junior"
        },

        {
            "title":"AI Engineer",
            "location":"Hybrid",
            "level":"Entry Level"
        },

        {
            "title":"Software Engineer",
            "location":"Remote",
            "level":"Graduate"
        }

    ]

    for job in jobs:

        with st.container():

            st.subheader(
                job["title"]
            )

            st.write(
                f"{job['location']} | {job['level']}"
            )

            if st.button(
                f"Apply {job['title']}",
                key=job["title"]
            ):

                try:

                    requests.post(
                        f"{API}/jobs/apply",
                        json={
                            "job":
                            job["title"],

                            "user":
                            st.session_state.user["name"]
                        }
                    )

                    st.session_state.applied_jobs.append(
                        job["title"]
                    )

                    st.session_state.history.append(
                        f"Applied : {job['title']}"
                    )

                    st.success(
                        "Application Submitted Successfully"
                    )

                except Exception as e:

                    st.error(
                        str(e)
                    )

            st.divider()