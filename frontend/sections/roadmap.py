import streamlit as st
from utils.api_client import ask_ai


def show_roadmap():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#0ea5e9,#2563eb);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>📚 AI Study Roadmap Generator</h1>
        <p>
        Generate a personalized learning roadmap based on
        your career goal, timeline, required skills,
        projects, and resources.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:

        goal = st.text_input(
            "🎯 Enter Career Goal",
            placeholder="Example: Software Engineer, Data Scientist, AI Engineer"
        )

        duration = st.selectbox(
            "⏳ Select Duration",
            [
                "1 Month",
                "3 Months",
                "6 Months",
                "1 Year"
            ]
        )

        generate_btn = st.button(
            "🚀 Generate Roadmap",
            use_container_width=True
        )

    with col2:

        st.info("""
        ### Roadmap Includes

        ✅ Weekly Plan

        ✅ Required Skills

        ✅ Learning Path

        ✅ Projects

        ✅ Resources

        ✅ Career Guidance
        """)

    if generate_btn:

        if not goal:
            st.warning("Please enter a career goal.")
            st.stop()

        prompt = f"""
        Create a complete learning roadmap.

        Goal:
        {goal}

        Duration:
        {duration}

        Include:

        1. Weekly Plan

        2. Skills To Learn

        3. Recommended Projects

        4. Free Learning Resources

        5. Career Advice

        Format neatly with headings.
        """

        progress = st.progress(0)

        with st.spinner("Generating Roadmap..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ Roadmap Generated Successfully")

            st.markdown("### 🗺️ Your Learning Roadmap")

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
            st.error(result.get("error", "Failed to generate roadmap"))
            