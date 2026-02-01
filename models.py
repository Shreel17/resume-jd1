# from pydantic import BaseModel
# from typing import List, Optional
# from pydantic import BaseModel, EmailStr

# class ResumeUpload(BaseModel):
#     resume_text: str
#     visibility: str  # public | private

# class JDRequest(BaseModel):
#     jd_text: str
#     db_type: str  # public | private

# class RecruiterAuth(BaseModel):
#     email: str
#     password: str

# class RefreshTokenRequest(BaseModel):
#     refresh_token: str

from pydantic import BaseModel, EmailStr
from typing import Optional, List


# ---------------- AUTH MODELS ---------------- #

class RecruiterAuth(BaseModel):
    email: EmailStr
    password: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ---------------- RESUME MODELS ---------------- #

class ResumeUploadResponse(BaseModel):
    resume_id: str
    visibility: str
    company: Optional[str]


# ---------------- JD MODELS ---------------- #

class JDMatchRequest(BaseModel):
    jd_text: str
    company: Optional[str] = None


class JDMatchResult(BaseModel):
    resume_id: str
    name: Optional[str]
    skills: List[str]
    experience: Optional[str]
    match_score: float