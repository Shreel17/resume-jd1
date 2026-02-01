# from chroma_client import get_collection
# from database import processed_resumes
# from embedding import generate_embedding
# from reranker import rerank


# def match_jd(jd_text: str, company: str | None = None):
#     """
#     Match a Job Description against public or company-private resumes.
#     Returns ranked, structured candidate profiles.
#     """

#     # ---------- Embed JD ----------
#     jd_embedding = generate_embedding(jd_text)

#     # ---------- Select vector collection ----------
#     collection_name = (
#         "public_resumes"
#         if not company
#         else f"private_{company}"
#     )
#     vector_collection = get_collection(collection_name)

#      # Filter by metadata
#     where_filter = {"visibility": "public"} if not company else {"company": company}

#     # ---------- Vector search ----------
#     results = vector_collection.query(
#         query_embeddings=[jd_embedding],
#         n_results=10
#         #high risk change
#         where=where_filter   # <= this filters resumes by metadata
#     )

#     resume_ids = results.get("ids", [[]])[0]

#     if not resume_ids:
#         return []

#     # ---------- Fetch processed resumes ----------
#     resumes = []
#     for resume_id in resume_ids:
#         doc = processed_resumes.find_one(
#             {"resume_id": resume_id}
#         )
#         if not doc:
#             continue

#         resumes.append({
#             "resume_id": resume_id,
#             "text": str(doc.get("structured", ""))
#         })

#     # ---------- Cross-encoder rerank ----------
#     ranked = rerank(jd_text, resumes)

#     # ---------- Final response ----------
#     final_results = []
#     for r in ranked:
#         doc = processed_resumes.find_one(
#             {"resume_id": r["resume_id"]}
#         )
#         if not doc:
#             continue

#         structured = doc.get("structured", {})

#         final_results.append({
#             "resume_id": r["resume_id"],
#             "name": structured.get("name"),
#             "skills": structured.get("skills"),
#             "experience": structured.get("experience"),
#             "match_score": round(r["rerank_score"] * 100, 2)
#         })

#     return final_results

from chroma_client import get_collection
from database import processed_resumes
from embedding import generate_embedding
from reranker import rerank

def sanitize_metadata(metadata: dict):
    """
    Replace None values in metadata with safe defaults for ChromaDB query.
    """
    sanitized = {}
    for k, v in metadata.items():
        if v is None:
            sanitized[k] = ""
        else:
            sanitized[k] = v
    return sanitized

def match_jd(jd_text: str, company: str | None = None):
    """
    Match a Job Description against public or company-private resumes.
    Returns ranked, structured candidate profiles.
    """

    # ---------- Embed JD ----------
    jd_embedding = generate_embedding(jd_text)

    # ---------- Vector search ----------
    vector_collection = get_collection("resumes")

    # Filter by metadata
    where_filter: dict[str, str] = {"visibility": "public"} if not company else {"company": company}
    where_filter=sanitize_metadata(where_filter)
    results = vector_collection.query(
        query_embeddings=[jd_embedding],
        n_results=10,
        where=where_filter  # type: ignore
)


    resume_ids = results.get("ids", [[]])[0]

    if not resume_ids:
        return []

    # ---------- Fetch processed resumes ----------
    resumes = []
    for resume_id in resume_ids:
        doc = processed_resumes.find_one({"resume_id": resume_id})
        if not doc:
            continue
        resumes.append({
            "resume_id": resume_id,
            "text": str(doc.get("structured", ""))
        })

    # ---------- Rerank ----------
    ranked = rerank(jd_text, resumes)

    # ---------- Final response ----------
    final_results = []
    for r in ranked:
        doc = processed_resumes.find_one({"resume_id": r["resume_id"]})
        if not doc:
            continue
        structured = doc.get("structured", {})
        final_results.append({
            "resume_id": r["resume_id"],
            "name": structured.get("name"),
            "skills": structured.get("skills"),
            "experience": structured.get("experience"),
            "match_score": round(r["rerank_score"] * 100, 2)
        })

    return final_results
