import streamlit as st
from frontend.api import signup, login

# def auth_page():
#     st.title("🔐 TalentSync – Recruiter Access")

#     tab1, tab2 = st.tabs(["Login", "Signup"])

#     with tab1:
#         email = st.text_input("Email")
#         password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             res = login(email, password)
#             if res.status_code == 200:
#                 st.session_state.token = res.json()["access_token"]
#                 st.success("Login successful")
#                 st.rerun()
#             else:
#                 st.error("Invalid credentials")

#     with tab2:
#         email = st.text_input("Signup Email")
#         password = st.text_input("Signup Password", type="password")
#         if st.button("Signup"):
#             res = signup(email, password)
#             if res.status_code == 200:
#                 st.success("Account created. Please login.")
#             else:
#                 st.error("User already exists")

def auth_page():
    st.title("🔐 TalentSync – Recruiter Access")

    if "auth_tab" not in st.session_state:
        st.session_state.auth_tab = "Login"

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            st.session_state.auth_tab = "Login"
    with col2:
        if st.button("Signup"):
            st.session_state.auth_tab = "Signup"

    st.markdown("---")

    if st.session_state.auth_tab == "Login":
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login Now"):
            res = login(email, password)
            if res.status_code == 200:
                st.session_state.token = res.json()["access_token"]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    else:
        email = st.text_input("Signup Email", key="signup_email")
        password = st.text_input("Signup Password", type="password", key="signup_pass")

        if st.button("Create Account"):
            res = signup(email, password)
            if res.status_code == 200:
                st.success("Signup successful. Please login.")
                st.session_state.auth_tab = "Login"
            else:
                st.error(res.text)



