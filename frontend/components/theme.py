# theme.py

import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    .stApp {
        background-color: #f9fafb;
        color: #111827;
    }

    h1, h2, h3 {
        color: #111827;
    }

    .stButton>button {
        background-color: #4F46E5;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
    }

    .stButton>button:hover {
        background-color: #4338CA;
    }

    textarea {
        border-radius: 10px !important;
    }

    </style>
    """, unsafe_allow_html=True)