import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


def show_register():

    st.title("📝 Register")

    name = st.text_input("Name")
    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Create Account"):

        response = requests.post(
            f"{BASE_URL}/register",
            json={
                "name": name,
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:
            st.success("Account Created")

        else:
            st.error("Registration Failed")
            