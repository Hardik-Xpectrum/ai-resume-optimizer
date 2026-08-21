from fastapi import APIRouter, UploadFile, File, Form

from app.services.parser_service import (
    extract_pdf_text,
    extract_docx_text,
)
from app.services.ats_service import analyze_resume

router = APIRouter(tags=["Resume Analysis"])


@router.post("/analyze-uploaded-resume")
async def analyze_uploaded_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...),
):
    # Validate file type
    if not file.filename:
        return {"error": "No file provided"}

    if not file.filename.lower().endswith((".pdf", ".docx")):
        return {
            "error": "Unsupported file type. Please upload PDF or DOCX."
        }

    # Save uploaded file
    upload_dir = "uploads"
    import os
    os.makedirs(upload_dir, exist_ok=True)

    file_path = f"{upload_dir}/{file.filename}"

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    # Extract resume text
    if file.filename.lower().endswith(".pdf"):
        resume_text = extract_pdf_text(file_path)
    else:
        resume_text = extract_docx_text(file_path)

    # Run ATS analysis
    result = analyze_resume(
        resume_text=resume_text,
        job_description=job_description,
    )

    return {
        "filename": file.filename,
        "ats_analysis": result,
    }