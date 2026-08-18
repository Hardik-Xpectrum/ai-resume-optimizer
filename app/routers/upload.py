from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.parser_service import (
    extract_pdf_text,
    extract_docx_text
)

router = APIRouter(tags=["Resume Upload"])


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file.filename.endswith(".pdf"):
        text = extract_pdf_text(file_path)

    elif file.filename.endswith(".docx"):
        text = extract_docx_text(file_path)

    else:
        return {
            "error": "Unsupported file type"
        }

    return {
        "filename": file.filename,
        "text": text[:2000]
    }