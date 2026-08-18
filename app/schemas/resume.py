from pydantic import BaseModel


class ResumeCreate(BaseModel):
    name: str
    skills: list[str]