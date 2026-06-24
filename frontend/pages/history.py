import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("📜 Activity History")

    st.info("AI interactions, resume analysis & job activity")

    # placeholder (backend connect later)
    st.write([
        "Resume analyzed - Score 82",
        "Asked AI: How to prepare for ML job",
        "Job applied: Google AI Engineer"
    ])