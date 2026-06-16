import streamlit as st
from utils.api_client import ask_ai


def show_interview():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#f97316,#ef4444);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>🎤 AI Interview Preparation</h1>
        <p>
        Generate role-specific interview questions,
        model answers, HR scenarios, and technical
        preparation guidance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        role = st.text_input(
            "💼 Target Job Role",
            placeholder="Software Engineer, Data Analyst, AI Engineer..."
        )

        level = st.selectbox(
            "📈 Experience Level",
            [
                "Fresher",
                "Intern",
                "1-2 Years",
                "3+ Years"
            ]
        )

        generate_btn = st.button(
            "🚀 Generate Interview Questions",
            use_container_width=True
        )

    with col2:

        st.info("""
### Interview Kit Includes

✅ Technical Questions

✅ HR Questions

✅ Scenario Questions

✅ Sample Answers

✅ Common Mistakes

✅ Preparation Tips
""")

    if generate_btn:

        if not role:
            st.warning("Please enter a target role.")
            st.stop()

        prompt = f"""
Act as a senior technical interviewer.

Role:
{role}

Experience Level:
{level}

Generate:

1. Technical Questions

2. HR Questions

3. Scenario-Based Questions

4. Sample Answers

5. Common Mistakes

6. Final Preparation Tips

Format professionally with headings.
"""

        progress = st.progress(0)

        with st.spinner("Preparing Interview Kit..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ Interview Questions Generated")

            st.markdown("### 🎯 Interview Preparation Kit")

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
                    "Unable to generate interview questions"
                )
            )