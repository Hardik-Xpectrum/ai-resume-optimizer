import re


# Skills that our ATS understands.
# We will expand this list as the project grows.
SKILL_ALIASES = {
    "python": ["python"],
    "sql": ["sql", "mysql", "postgresql", "postgres", "t-sql"],
    "pyspark": ["pyspark"],
    "spark": ["apache spark", "spark"],
    "databricks": ["databricks"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["gcp", "google cloud", "google cloud platform"],
    "airflow": ["airflow", "apache airflow"],
    "snowflake": ["snowflake"],
    "dbt": ["dbt"],
    "terraform": ["terraform"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "fastapi": ["fastapi"],
    "django": ["django"],
    "java": ["java"],
    "scala": ["scala"],
    "etl": ["etl", "etl pipelines", "extract transform load"],
    "elt": ["elt"],
    "data warehousing": [
        "data warehouse",
        "data warehousing",
        "data warehouse architecture",
    ],
    "data lake": [
        "data lake",
        "data lakes",
    ],
    "lakehouse": [
        "lakehouse",
        "lakehouse architecture",
    ],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "git": ["git"],
    "github": ["github"],
    "linux": ["linux"],
}


def normalize_text(text: str) -> str:
    """
    Normalize text for consistent skill matching.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_skills(text: str) -> set[str]:
    """
    Extract recognized technical/business skills from text.
    """

    normalized_text = normalize_text(text)

    found_skills = set()

    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias in normalized_text:
                found_skills.add(skill)
                break

    return found_skills


def analyze_resume(
    resume_text: str,
    job_description: str,
):
    """
    Analyze resume against a job description.
    """

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills

    if not jd_skills:
        score = 0
    else:
        score = round(
            len(matched_skills) / len(jd_skills) * 100
        )

    recommendations = [
        f"Consider adding '{skill}'"
        for skill in sorted(missing_skills)
    ]

    return {
        "ats_score": score,
        "resume_skills": sorted(resume_skills),
        "required_skills": sorted(jd_skills),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "recommendations": recommendations,
    }