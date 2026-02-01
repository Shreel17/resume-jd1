import streamlit as st
import plotly.express as px
import pandas as pd

def analytics_page():
    st.header("📊 Resume Analytics")

    data = {
        "Category": ["Public", "Private"],
        "Count": [42, 28]
    }
    df = pd.DataFrame(data)

    fig = px.pie(df, values="Count", names="Category", title="Resume Visibility")
    st.plotly_chart(fig, use_container_width=True)

    skills = ["Python", "ML", "FastAPI", "MongoDB"]
    counts = [30, 20, 18, 15]
    skill_df = pd.DataFrame({"Skill": skills, "Count": counts})

    bar = px.bar(skill_df, x="Skill", y="Count", title="Top Skills")
    st.plotly_chart(bar, use_container_width=True)