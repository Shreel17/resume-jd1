import streamlit as st
from frontend.api import match_jd

def jd_page():
    st.header("📌 Job Description Matching")

    jd_text = st.text_area("Paste Job Description")
    company = st.text_input("Company (leave blank for public)")

    if st.button("Match"):
        res = match_jd(jd_text, company or None, st.session_state.token)
        if res.status_code == 200:
            for r in res.json():
                with st.expander(r["name"] or "Candidate"):
                    st.write("Skills:", r["skills"])
                    st.write("Experience:", r["experience"])

                    st.metric("Match Score", f"{r['match_score']}%")
