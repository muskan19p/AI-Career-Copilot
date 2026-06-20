import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


def show_login():

    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        response = requests.post(
            f"{BASE_URL}/login",
            json={
                "email": email,
                "password": password
            }
        )

        data = response.json()

        if data["success"]:

            st.session_state.logged_in = True
            st.session_state.user_id = data["user_id"]
            st.session_state.username = data["name"]

            st.success("Login Successful")
            st.rerun()

        else:
            st.error(data["message"])