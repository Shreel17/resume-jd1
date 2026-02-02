import streamlit as st
from frontend.api import signup, login

def auth_page():
    st.title("🔐 TalentSync – Recruiter Access")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            res = login(email, password)
            if res.status_code == 200:
                st.session_state.token = res.json()["access_token"]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        email = st.text_input("Signup Email")
        password = st.text_input("Signup Password", type="password")
        if st.button("Signup"):
            res = signup(email, password)
            if res.status_code == 200:
                st.success("Account created. Please login.")
            else:
                st.error("User already exists")

