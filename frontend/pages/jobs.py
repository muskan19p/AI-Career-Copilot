import streamlit as st

def show():

    st.title("💼 Job Recommendations")

    jobs = [
        "Python Developer",
        "Backend Developer",
        "AI Engineer",
        "Software Engineer"
    ]

    for job in jobs:

        with st.container():

            st.subheader(job)

            st.write(
                "Remote | Entry Level"
            )

            st.button(
                f"Apply {job}",
                key=job
            )