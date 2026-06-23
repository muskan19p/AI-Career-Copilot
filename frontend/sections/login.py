import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


def show_login():

    st.title("🔐 Login to Career OS")

    email = st.text_input(
        "📧 Email",
        key="login_email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "🚀 Login",
        use_container_width=True
    ):

        if not email:
            st.error("Email is required")
            return

        if not password:
            st.error("Password is required")
            return

        try:

            response = requests.post(
                f"{BASE_URL}/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            data = response.json()

            if data.get("success"):

                st.session_state.logged_in = True

                st.session_state.user_id = data["user_id"]

                st.session_state.username = data["name"]

                st.success("Login Successful")

                st.session_state.page = "🏠 Dashboard"

                st.rerun()

            else:

                st.error(
                    data.get(
                        "message",
                        "Login Failed"
                    )
                )

        except Exception as e:

            st.error(
                f"Server Error: {str(e)}"
            )

    st.markdown("---")

    if st.button(
        "📝 Create New Account",
        use_container_width=True
    ):

        st.session_state.page = "📝 Register"

        st.rerun()