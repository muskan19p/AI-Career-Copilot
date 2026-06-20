import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


def show_history():

    st.title("📚 Analysis History")

    user_id = st.session_state.user_id

    response = requests.get(
        f"{BASE_URL}/history/{user_id}"
    )

    data = response.json()

    history = data["history"]

    if not history:
        st.info("No History Found")
        return

    for item in history:

        with st.expander(
            f"Analysis #{item['id']}"
        ):

            st.write(item["analysis"])

            if st.button(
                f"Delete {item['id']}"
            ):

                requests.delete(
                    f"{BASE_URL}/history/{item['id']}"
                )

                st.rerun()
                