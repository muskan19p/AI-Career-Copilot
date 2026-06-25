import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("🚀 Career OS - Login")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    # ---------------- LOGIN ----------------
    with tab1:

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):

            res = requests.post(f"{API}/auth/login", json={
                "email": email,
                "password": password
            })

            data = res.json()

            if data.get("success"):

                st.session_state.user = data["user"]
                st.success("Login successful 🚀")
                st.rerun()

            else:
                st.error("Invalid credentials")

    # ---------------- SIGNUP ----------------
    with tab2:

        name = st.text_input("Name", key="signup_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")

        if st.button("Create Account"):

            res = requests.post(f"{API}/auth/register", json={
                "name": name,
                "email": email,
                "password": password
            })

            data = res.json()

            if data.get("success"):
               st.success(
                     "Account Created Successfully 🚀"
                       )

               st.info(
                     "Please Login"
                      )

               st.rerun()
            else:
                st.error("Signup failed")