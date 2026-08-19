from fastapi import FastAPI

from app.routers.resume import router as resume_router
from app.routers.upload import router as upload_router
from app.routers.ats import router as ats_router

app = FastAPI()

app.include_router(resume_router)
app.include_router(upload_router)
app.include_router(ats_router)


@app.get("/")
def root():
    return {"message": "AI Resume Optimizer API"}