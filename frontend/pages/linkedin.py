import streamlit as st

def show():

    st.title("🔗 LinkedIn Optimizer")

    headline = st.text_input(
        "Current Headline"
    )

    if st.button("Generate Better Headline"):

        st.success(
            "Python Developer | FastAPI Developer | AI Enthusiast | Open to Work"
        )
        