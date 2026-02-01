from database import recruiters_collection
from auth_utils import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token
)
from datetime import datetime
import uuid

def signup_recruiter(email: str, password: str):
    recruiter_id = str(uuid.uuid4())
    try:
    
        recruiters_collection.insert_one({
        "recruiter_id": recruiter_id,
        "email": email,
        "password": hash_password(password),
        "created_at": datetime.utcnow()
    })
    except Exception as e:
        raise e 
    payload = {"sub": recruiter_id}
    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload)
    }

def login_recruiter(email: str, password: str):
    recruiter = recruiters_collection.find_one({"email": email})
    if not recruiter:
        return None

    if not verify_password(password, recruiter["password"]):
        return None
    
    recruiter_id = recruiter["recruiter_id"]  #define it
    payload = {"sub": recruiter_id}
    return {
        "recruiter_id": recruiter_id,
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload)
    }
