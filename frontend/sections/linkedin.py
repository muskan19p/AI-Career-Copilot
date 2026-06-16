import streamlit as st
from utils.api_client import ask_ai


def show_linkedin():

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#0077B5,#2563eb);
        padding:25px;
        border-radius:18px;
        color:white;
        margin-bottom:20px;
    ">
        <h1>🔗 LinkedIn Profile Optimizer</h1>
        <p>
        Improve your LinkedIn visibility with an optimized
        headline, professional summary, and recruiter-friendly
        keywords.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        headline = st.text_input(
            "💼 Current Headline",
            placeholder="Example: Software Engineer | Python Developer"
        )

        about = st.text_area(
            "📝 About Section",
            height=220,
            placeholder="Paste your LinkedIn About section..."
        )

        optimize_btn = st.button(
            "🚀 Optimize Profile",
            use_container_width=True
        )

    with col2:

        st.info("""
### Optimization Includes

✅ Professional Headline

✅ About Section Rewrite

✅ SEO Keywords

✅ Recruiter Visibility

✅ Industry Positioning

✅ Personal Branding
""")

    if optimize_btn:

        if not headline and not about:
            st.warning("Please enter headline or about section.")
            st.stop()

        prompt = f"""
Improve LinkedIn Profile.

Current Headline:
{headline}

About Section:
{about}

Provide:

1. Optimized Headline

2. Optimized About Section

3. SEO Keywords

4. Profile Improvement Suggestions

5. Recruiter Visibility Tips

Format professionally.
"""

        progress = st.progress(0)

        with st.spinner("Optimizing LinkedIn Profile..."):

            for i in range(100):
                progress.progress(i + 1)

            result = ask_ai(prompt)

        if result.get("success"):

            st.success("✅ LinkedIn Profile Optimized")

            st.markdown("### 🔥 Optimization Results")

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
                    "Unable to optimize profile"
                )
            )
            