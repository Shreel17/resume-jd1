import streamlit as st
from api import upload_resumes

def upload_page():
    st.header("📤 Upload Resumes")

    db_type = st.radio("Database Type", ["Public", "Private"])
    visibility = "public" if db_type == "Public" else "private"
    company = None
    if visibility == "private":
        company = st.text_input("Company Name")


    files = st.file_uploader(
        "Upload resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("Upload"):
        if not files:
            st.warning("Please upload at least one resume")
            return

        payload = []
        for f in files:
            payload.append(
                (
                    "files",
                    (f.name, f.getvalue(), f.type)  # ✅ IMPORTANT
                )
            )

        res = upload_resumes(
            files=payload,
            company=company,
            visibility=visibility,
            token=st.session_state.token
        )

        if res.status_code == 200:
            st.success("Resumes uploaded successfully")
        else:
            st.error(f"Upload failed: {res.text}")