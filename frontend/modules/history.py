import streamlit as st

def show():

    st.title("📜 Activity History")

    history = st.session_state.get(
        "history",
        []
    )

    if not history:

        st.warning(
            "No activity found"
        )
        return

    for item in reversed(history):

        st.info(item)

    st.divider()

    if st.button(
        "Clear History"
    ):

        st.session_state.history = []

        st.success(
            "History Cleared"
        )

        st.rerun()