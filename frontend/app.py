import streamlit as st
# Purane imports ko replace karein:
from frontend.auth import auth_page
from frontend.dashboard import dashboard
from frontend.upload import upload_page
from frontend.jd_match import jd_page
from frontend.analytics import analytics_page
from frontend.styles import inject_custom_css

st.set_page_config(
    page_title="TalentSync",
    page_icon="🧠",
    layout="wide"
)

inject_custom_css()   # <-- ADD THIS LINE ONLY

if "token" not in st.session_state:
    auth_page()
else:
    st.sidebar.title("TalentSync")
    choice = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Upload Resumes", "JD Matching", "Analytics", "Logout"]
    )

    if choice == "Dashboard":
        dashboard()
    elif choice == "Upload Resumes":
        upload_page()
    elif choice == "JD Matching":
        jd_page()
    elif choice == "Analytics":
        analytics_page()
    else:
        del st.session_state["token"]
        st.rerun()



