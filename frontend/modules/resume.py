import streamlit as st
import requests
from io import BytesIO

API = "http://127.0.0.1:8000"

# optional libs for parsing
import docx
from pypdf import PdfReader



def extract_text(file, file_type):

    if file_type == "txt":
        return file.read().decode("utf-8")

    elif file_type == "pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif file_type == "docx":
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    return ""


def show():

    st.title("📄 AI Resume Builder")

    # ---------------- INPUT ----------------
    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"]
    )

    manual_text = st.text_area("Or Paste Resume")

    text = ""

    # ---------------- FILE HANDLING ----------------
    if uploaded_file:
        try:
            file_type = uploaded_file.name.split(".")[-1].lower()
            text = extract_text(uploaded_file, file_type)

            st.success(f"{uploaded_file.name} Uploaded & Parsed")

        except Exception as e:
            st.error(f"File Error: {str(e)}")

    elif manual_text:
        text = manual_text

    # ---------------- AI GENERATE (FAKE OR BACKEND READY) ----------------
    if st.button("Generate Resume with AI"):

        if not text:
            st.warning("Upload or Paste Resume First")
            return

        with st.spinner("AI is optimizing your resume..."):

            # TODO: connect real backend AI
            st.success("AI Resume Generated ✨")

            st.markdown("""
            ### 🚀 Optimized Resume
            - Strong action verbs added
            - ATS keywords improved
            - Format cleaned
            - Industry-ready structure
            """)

    # ---------------- ATS ANALYSIS ----------------
    if st.button("Analyze Resume"):

        if not text:
            st.warning("Upload or Paste Resume")
            return

        try:
            res = requests.post(
                f"{API}/resume/analyze",
                json={"text": text}
            )

            data = res.json()

            st.session_state.ats_count += 1
            st.session_state.history.append("Resume Analyzed")

            st.subheader("📊 ATS Score")
            st.metric("Score", data.get("ats_score", 0))

            st.subheader("🧠 Skills")
            st.write(data.get("skills", []))

            st.subheader("💡 Suggestions")
            st.write(data.get("improvements", []))

        except Exception as e:
            st.error(f"API Error: {str(e)}")