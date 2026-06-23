import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


def show_register():

    st.title("📝 Create Career OS Account")

    username = st.text_input(
        "👤 Username",
        key="reg_username"
    )

    email = st.text_input(
        "📧 Email",
        key="reg_email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="reg_password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password",
        key="reg_confirm_password"
    )

    if st.button(
        "🚀 Create Account",
        use_container_width=True
    ):

        if not username:
            st.error("Username is required")
            return

        if not email:
            st.error("Email is required")
            return

        if not password:
            st.error("Password is required")
            return

        if password != confirm_password:
            st.error("Passwords do not match")
            return

        try:

            response = requests.post(
                f"{BASE_URL}/register",
                json={
                    "name": username,
                    "email": email,
                    "password": password
                }
            )

            data = response.json()

            if data.get("success"):

                st.success(
                    data.get(
                        "message",
                        "Account Created Successfully"
                    )
                )

                st.session_state.page = "🔐 Login"

                st.rerun()

            else:

                st.error(
                    data.get(
                        "message",
                        "Registration Failed"
                    )
                )

        except Exception as e:

            st.error(
                f"Server Error: {str(e)}"
            )

    st.markdown("---")

    if st.button(
        "🔐 Already have an account? Login",
        use_container_width=True
    ):
        st.session_state.page = "🔐 Login"
        st.rerun()
        
        
        