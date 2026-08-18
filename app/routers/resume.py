from fastapi import APIRouter

from app.schemas.resume import ResumeCreate
from app.services.resume_service import (
    get_all_resumes,
    create_resume,
)

router = APIRouter()


@router.get("/resumes")
def get_resumes():
    return get_all_resumes()


@router.post("/resumes")
def upload_resume(resume: ResumeCreate):
    return create_resume(
        name=resume.name,
        skills=resume.skills
    )
