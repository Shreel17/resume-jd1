import streamlit as st

# def apply_styles():
#     st.markdown("""
#     <style>
#     .card {
#         padding: 20px;
#         border-radius: 15px;
#         background: #ffffff;
#         box-shadow: 0 4px 14px rgba(0,0,0,0.1);
#         transition: 0.3s ease-in-out;
#     }
#     .card:hover {
#         transform: scale(1.03);
#         box-shadow: 0 6px 20px rgba(0,0,0,0.2);
#     }
#     </style>
#     """, unsafe_allow_html=True)

def inject_custom_css():
    st.markdown("""
        <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #020617, #0f172a);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #020617, #020617);
            border-right: 1px solid #1e293b;
        }

        /* Sidebar title */
        section[data-testid="stSidebar"] h1 {
            color: #14b8a6;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        /* Radio buttons */
        div[role="radiogroup"] label {
            padding: 8px;
            border-radius: 8px;
            transition: all 0.2s ease;
        }

        div[role="radiogroup"] label:hover {
            background-color: rgba(20, 184, 166, 0.15);
        }

        /* Cards / Containers */
        .block-container {
            padding-top: 2rem;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #14b8a6, #0ea5e9);
            color: white;
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            border: none;
            font-weight: 600;
            transition: all 0.2s ease;
        }

        .stButton>button:hover {
            transform: scale(1.03);
            box-shadow: 0px 6px 18px rgba(20, 184, 166, 0.35);
        }

        /* Inputs */
        input, textarea {
            border-radius: 10px !important;
            background-color: #020617 !important;
            color: #e5e7eb !important;
        }

        /* Tables */
        .stDataFrame {
            border-radius: 12px;
            overflow: hidden;
        }

        </style>
    """, unsafe_allow_html=True)
