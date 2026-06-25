import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("🧠 AI Career Mentor")

    goal = st.text_input(
        "Your Career Goal"
    )

    if st.button(
        "Generate Roadmap"
    ):

        if goal.strip() == "":

            st.warning(
                "Enter Career Goal"
            )

        else:

            try:

                res = requests.post(
                    f"{API}/ai/resume-review",
                    json={
                        "text":
                        f"Create roadmap for {goal}"
                    }
                )

                answer = res.json()["answer"]

                st.session_state.roadmap_count += 1

                st.session_state.history.append(
                    f"Roadmap Generated : {goal}"
                )

                st.success(
                    answer
                )

            except Exception as e:

                st.error(
                    str(e)
                )