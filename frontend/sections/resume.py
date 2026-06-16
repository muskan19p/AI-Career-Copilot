import streamlit as st
from utils.api_client import analyze_resume


def show_resume():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#2563eb,#7c3aed);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>📄 Resume Analyzer</h1>
        <p>
        Upload your resume and receive AI-powered feedback,
        improvement suggestions, ATS optimization tips,
        and professional recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:

        uploaded_file = st.file_uploader(
            "Upload Resume",
            type=["pdf", "docx"]
        )

        analyze_btn = st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        )

    with col2:

        st.info("""
        ### Analysis Includes

        ✅ Resume Review

        ✅ Skill Gap Detection

        ✅ ATS Optimization

        ✅ Content Suggestions

        ✅ Professional Feedback
        """)

    if uploaded_file and analyze_btn:

        progress = st.progress(0)

        with st.spinner("Analyzing Resume..."):

            for i in range(100):
                progress.progress(i + 1)

            result = analyze_resume(uploaded_file)

        if result.get("success"):

            st.success("✅ Resume Analysis Complete")

            st.markdown("### 📊 Analysis Report")

            st.markdown(f"""
            <div style="
                background:white;
                padding:20px;
                border-radius:15px;
                border:1px solid #e5e7eb;
            ">
            {result["analysis"]}
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error(result.get("error", "Something went wrong"))
            