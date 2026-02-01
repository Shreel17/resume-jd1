from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Raw resumes collection
raw_resumes = db.raw_resumes
raw_resumes.create_index("resume_id", unique=True)
raw_resumes.create_index("visibility")
raw_resumes.create_index("recruiter_id")

# Processed resumes collection
processed_resumes = db.processed_resumes
processed_resumes.create_index("resume_id", unique=True)
processed_resumes.create_index("visibility")
processed_resumes.create_index("recruiter_id")

recruiters_collection = db.recruiters
recruiters_collection.create_index("email", unique=True)
