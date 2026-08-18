resumes = []


def get_all_resumes():
    return resumes


def create_resume(name: str, skills: list[str]):
    resume = {
        "id": len(resumes) + 1,
        "name": name,
        "skills": skills,
        "status": "uploaded"
    }

    resumes.append(resume)
    return resume