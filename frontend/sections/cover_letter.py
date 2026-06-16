import streamlit as st
from utils.api_client import ask_ai


def show_cover_letter():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#ec4899,#8b5cf6);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>✉️ AI Cover Letter Generator</h1>
        <p>
        Create personalized, professional, and recruiter-friendly
        cover letters tailored to your target role and company.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        company = st.text_input(
            "🏢 Company Name",
            placeholder="Google, Microsoft, Amazon..."
        )

        role = st.text_input(
            "💼 Job Role",
            placeholder="Software Engineer, Data Analyst..."
        )

        skills = st.text_area(
            "🛠️ Your Skills",
            height=180,
            placeholder="""
Python
SQL
Machine Learning
FastAPI
Streamlit
AWS
Git
"""
        )

        generate_btn = st.button(
            "🚀 Generate Cover Letter",
            use_container_width=True
        )

    with col2:

        st.info("""
### Cover Letter Includes

✅ Professional Introduction

✅ Role Alignment

✅ Skills Highlight

✅ Company Fit

✅ Strong Closing

✅ Recruiter-Friendly Format
""")

    if generate_btn:

        if not company or not role:
            st.warning("Please enter company and role.")
            st.stop()

        prompt = f"""
Generate a professional cover letter.

Company:
{company}

Role:
{role}

Skills:
{skills}

Include:

1. Professional Introduction

2. Relevant Skills

3. Why I Fit The Role

4. Why I Want To Join Company

5. Strong Closing Statement

Keep it professional and ATS-friendly.
"""

        progress = st.progress(0)

        with st.spinner("Generating Cover Letter..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ Cover Letter Generated")

            st.markdown("### 📄 Generated Cover Letter")

            st.markdown(f"""
            <div style="
                background:white;
                padding:20px;
                border-radius:15px;
                border:1px solid #e5e7eb;
                line-height:1.8;
            ">
            {result["response"]}
            </div>
            """, unsafe_allow_html=True)

            st.download_button(
                "⬇️ Download Cover Letter",
                result["response"],
                file_name="cover_letter.txt",
                mime="text/plain"
            )

        else:

            st.error(
                result.get(
                    "error",
                    "Unable to generate cover letter"
                )
            )
            