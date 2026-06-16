import streamlit as st
from utils.api_client import ask_ai


def show_jobs():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#10b981,#2563eb);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>💼 AI Job Recommendations</h1>
        <p>
        Discover suitable career paths, job roles,
        salary expectations, required skills,
        and growth opportunities based on your profile.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        skills = st.text_area(
            "🛠️ Your Skills",
            height=150,
            placeholder="""
Example:
Python, SQL, Machine Learning,
Data Analysis, FastAPI,
Streamlit, Git, AWS
"""
        )

        education = st.text_input(
            "🎓 Education",
            placeholder="B.Tech CSE, MCA, BCA, etc."
        )

        recommend_btn = st.button(
            "🚀 Get Job Recommendations",
            use_container_width=True
        )

    with col2:

        st.info("""
### Recommendation Includes

✅ Suitable Job Roles

✅ Salary Estimates

✅ Missing Skills

✅ Career Growth

✅ Industry Demand

✅ Learning Suggestions
""")

    if recommend_btn:

        if not skills.strip():
            st.warning("Please enter your skills.")
            st.stop()

        prompt = f"""
Act as an expert career advisor.

Skills:
{skills}

Education:
{education}

Provide:

1. Best Job Roles

2. Estimated Salary Range

3. Required Missing Skills

4. Career Growth Opportunities

5. Learning Recommendations

6. Hiring Industries

Format professionally with headings.
"""

        progress = st.progress(0)

        with st.spinner("Finding Best Career Opportunities..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ Recommendations Generated")

            st.markdown("### 🎯 Recommended Career Paths")

            st.markdown(f"""
            <div style="
                background:white;
                padding:20px;
                border-radius:15px;
                border:1px solid #e5e7eb;
            ">
            {result["response"]}
            </div>
            """, unsafe_allow_html=True)

        else:

            st.error(
                result.get(
                    "error",
                    "Unable to generate recommendations"
                )
            )