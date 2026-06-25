import streamlit as st

def show():

    st.title("🔗 LinkedIn Optimizer")

    headline = st.text_input(
        "Current Headline"
    )

    if st.button(
        "Generate Better Headline"
    ):

        if not headline:

            st.warning(
                "Enter Current Headline"
            )

            return

        optimized = f"""
Python Developer | FastAPI Developer |
AI Enthusiast | Machine Learning |
Open To Work
"""

        st.success(
            optimized
        )

        st.session_state.history.append(
            "LinkedIn Optimized"
        )