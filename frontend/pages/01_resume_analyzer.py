import streamlit as st
from utils.api_client import analyze_resume

st.header("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file:

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(uploaded_file)

            if result.get("success"):
                st.success("Analysis Complete")
                st.write(result["analysis"])
            else:
                st.error(result.get("error"))
                