import streamlit as st
from frontend.styles import inject_custom_css

def dashboard():
    inject_custom_css()
    st.title("🧠 TalentSync Recruiter Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>📤 Upload Resumes</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>📌 JD Matching</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>📊 Analytics</div>", unsafe_allow_html=True)

