from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(jd, resumes):
    pairs = [(jd, r["text"]) for r in resumes]
    scores = model.predict(pairs)

    for i, s in enumerate(scores):
        resumes[i]["rerank_score"] = float(s)

    return sorted(resumes, key=lambda x: x["rerank_score"], reverse=True)