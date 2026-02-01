from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from jd_matcher import match_jd
from dependencies import get_current_recruiter

router = APIRouter(prefix="/jd", tags=["JD"])

class JDMatchRequest(BaseModel):
    jd_text: str
    company: Optional[str] = None
    database_type: str  # "public" | "private"

# @router.post("/match")
# def match(
#     data: JDMatchRequest,
#     recruiter_id: str = Depends(get_current_recruiter)
# ):
#     return match_jd(
#         jd_text=data.jd_text,
#         company=data.company,
#         )
@router.post("/match")
def match(data: JDMatchRequest):
    return match_jd(
        jd_text=data.jd_text,
        company=data.company
    )

