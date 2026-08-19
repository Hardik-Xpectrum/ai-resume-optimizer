from fastapi import APIRouter

from app.schemas.ats import ATSRequest
from app.services.ats_service import analyze_resume

router = APIRouter(tags=["ATS Analyzer"])


@router.post("/analyze-resume")
def analyze(data: ATSRequest):
    return analyze_resume(
        resume_text=data.resume_text,
        job_description=data.job_description
    )