import streamlit as st

def show():

    st.title("📊 Career Dashboard")

    user = st.session_state.user

    st.subheader(
        f"Welcome {user['name']}"
    )

    st.write(
        f"📧 {user['email']}"
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Applications",
        len(st.session_state.get("applied_jobs", []))
    )

    c2.metric(
        "ATS Checks",
        st.session_state.get("ats_count", 0)
    )

    c3.metric(
        "AI Chats",
        len(st.session_state.get("chat_history", []))
    )

    c4.metric(
        "Roadmaps",
        st.session_state.get("roadmap_count", 0)
    )

    st.divider()

    st.subheader("🎯 Career Progress")

    st.progress(80)
    st.write("Python : 80%")

    st.progress(70)
    st.write("SQL : 70%")

    st.progress(65)
    st.write("FastAPI : 65%")

    st.divider()

    st.subheader("📌 Recent Activity")

    history = st.session_state.get(
        "history",
        []
    )

    if history:

        for item in reversed(history[-5:]):

            st.info(str(item))

    else:

        st.warning(
            "No activity yet"
        )