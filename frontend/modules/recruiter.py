import streamlit as st
import requests

API = "http://127.0.0.1:8000"

def show():

    st.title("👔 Recruiter Panel")

    res = requests.get(f"{API}/recruiter/candidates")

    st.write(res.json())