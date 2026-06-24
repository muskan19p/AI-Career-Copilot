import streamlit as st

def show():

    st.title("📊 Career Dashboard")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Resume Score","82%","+5")
    c2.metric("ATS Score","76%","+3")
    c3.metric("Applications","12","+2")
    c4.metric("Interviews","3","+1")

    st.divider()

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Career Progress")

        st.progress(80)
        st.write("Python : 80%")

        st.progress(70)
        st.write("SQL : 70%")

        st.progress(65)
        st.write("FastAPI : 65%")

    with col2:
        st.subheader("📌 Activity")

        st.success("Resume Uploaded")
        st.info("ATS Checked")
        st.warning("2 Jobs Saved")