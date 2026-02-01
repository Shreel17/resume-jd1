from typing import List, Optional

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends,
    HTTPException
)

from resume_service import (
    upload_resumes_service,
    update_resume_service,
    delete_resume_service
)

from dependencies import get_current_recruiter

router = APIRouter(prefix="/resumes", tags=["Resumes"])


# ======================= UPLOAD =======================

@router.post("/upload")
async def upload_resumes(
    files: List[UploadFile] = File(...),
    visibility: str = Form(...),      # public | private
    company: Optional[str] = Form(None),
    # recruiter_id: Optional[str] = Depends(get_current_recruiter)
):
    try:
        return upload_resumes_service(
            files=files,
            visibility=visibility,
            company=company,
            recruiter_id=None
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ======================= UPDATE =======================

@router.put("/{resume_id}")
async def update_resume(
    resume_id: str,
    file: UploadFile = File(...),
    recruiter_id: str = Depends(get_current_recruiter)
):
    try:
        return update_resume_service(
            resume_id=resume_id,
            file=file,
            recruiter_id=recruiter_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# ======================= DELETE =======================

@router.delete("/{resume_id}")
async def delete_resume(
    resume_id: str,
    recruiter_id: str = Depends(get_current_recruiter)
):
    try:
        return delete_resume_service(
            resume_id=resume_id,
            recruiter_id=recruiter_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))



