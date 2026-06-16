import streamlit as st
from utils.api_client import ask_ai


def show_mentor():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#7c3aed,#2563eb);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>🤖 AI Career Mentor</h1>
        <p>
        Get personalized career guidance, job search advice,
        skill recommendations, interview strategies,
        and long-term career planning support.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        query = st.text_area(
            "💬 Ask Your Career Question",
            height=180,
            placeholder="""
Examples:

• How can I become a Software Engineer?

• Which skills should I learn in 2026?

• How can I prepare for product-based companies?

• How do I switch from support to development?
"""
        )

        ask_btn = st.button(
            "🚀 Get Career Advice",
            use_container_width=True
        )

    with col2:

        st.info("""
### Mentor Can Help With

✅ Career Planning

✅ Skill Development

✅ Resume Guidance

✅ Job Search Strategy

✅ Interview Preparation

✅ Salary Growth

✅ Career Switching

✅ Industry Trends
""")

    if ask_btn:

        if not query.strip():
            st.warning("Please enter a question.")
            st.stop()

        prompt = f"""
Act as an expert career mentor.

Question:
{query}

Provide:

1. Direct Answer

2. Career Advice

3. Action Plan

4. Common Mistakes

5. Next Steps
"""

        progress = st.progress(0)

        with st.spinner("Generating Career Advice..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ Career Guidance Generated")

            st.markdown("### 🎯 Mentor Recommendations")

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
                    "Unable to generate advice"
                )
            )