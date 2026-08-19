import re


def extract_keywords(text: str):
    """
    Extract words from text.
    """

    words = re.findall(r"\b[a-zA-Z+#]+\b", text.lower())

    return set(words)


def analyze_resume(
    resume_text: str,
    job_description: str
):
    resume_keywords = extract_keywords(resume_text)

    jd_keywords = extract_keywords(job_description)

    matched = resume_keywords.intersection(jd_keywords)

    missing = jd_keywords - resume_keywords

    if len(jd_keywords) == 0:
        score = 0
    else:
        score = int(
            len(matched) / len(jd_keywords) * 100
        )

    recommendations = [
        f"Consider adding '{skill}'"
        for skill in list(missing)[:10]
    ]

    return {
        "ats_score": score,
        "matched_skills": sorted(list(matched)),
        "missing_skills": sorted(list(missing)),
        "recommendations": recommendations
    }