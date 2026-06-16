import streamlit as st
from utils.api_client import ask_ai


def show_ats():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#f59e0b,#ef4444);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>📊 ATS Score Checker</h1>
        <p>
        Analyze your resume compatibility with job descriptions
        and improve your chances of passing ATS filters.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:

        job_description = st.text_area(
            "📄 Paste Job Description",
            height=220,
            placeholder="Paste full job description here..."
        )

        check_btn = st.button(
            "🚀 Check ATS Score",
            use_container_width=True
        )

    with col2:

        st.info("""
### ATS Analysis Includes

🎯 ATS Score (0-100)

🔑 Important Keywords

❌ Missing Skills

💡 Optimization Tips

📈 Resume Improvement Guide
""")

    if check_btn:

        if not job_description.strip():
            st.warning("Please paste a job description.")
            st.stop()

        prompt = f"""
You are an ATS (Applicant Tracking System) expert.

Analyze the following job description and evaluate resume compatibility.

Job Description:
{job_description}

Provide output in this format:

1. ATS Score (0-100) with explanation
2. Important Keywords (bullet list)
3. Missing Skills
4. Suggestions to improve ATS score
5. Resume optimization tips
"""

        progress = st.progress(0)

        with st.spinner("Analyzing ATS compatibility..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ ATS Analysis Complete")

            st.markdown("### 📊 ATS Report")

            st.markdown(f"""
            <div style="
                background:white;
                padding:20px;
                border-radius:15px;
                border:1px solid #e5e7eb;
                line-height:1.6;
            ">
            {result["response"]}
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error(
                result.get(
                    "error",
                    "Failed to analyze ATS score"
                )
            )