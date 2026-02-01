# import re
# from rapidfuzz import fuzz

# def clean_text(text: str) -> str:
#     text = re.sub(r"\s+", " ", text)
#     return text.lower().strip()

# def extract_skills(text: str) -> list:
#     skills = ["python", "fastapi", "mongodb", "sql", "ml", "ai"]
#     return [s for s in skills if s in text]

# def skill_match_score(jd_skills, resume_skills):
#     if not jd_skills:
#         return 1.0
#     matched = set(jd_skills) & set(resume_skills)
#     return len(matched) / len(jd_skills)

# def title_match_score(jd, resume):
#     return fuzz.partial_ratio(jd, resume) / 100

import re
import zipfile
import pdfplumber
import docx

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return " ".join(p.extract_text() or "" for p in pdf.pages)
    if file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return " ".join(p.text for p in doc.paragraphs)
    return ""

def unzip(path, extract_to):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)