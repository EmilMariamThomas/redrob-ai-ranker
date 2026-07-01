def safe_get(d, key, default=None):
    if isinstance(d, dict):
        return d.get(key, default)
    return default


# ---------------------------
# NAME EXTRACTION (FIXED)
# ---------------------------
def extract_name(raw):

    if not isinstance(raw, dict):
        return "Unknown"

    profile = raw.get("profile")

    if isinstance(profile, dict):

        # PRIMARY NAME (your dataset)
        name = profile.get("anonymized_name")
        if name:
            return name

        # fallback options
        if profile.get("name"):
            return profile["name"]

        if profile.get("current_title"):
            return profile["current_title"]

    return "Unknown"


# ---------------------------
# SKILL CLEANING
# ---------------------------
def extract_skills(skills):

    if not isinstance(skills, list):
        return []

    clean = []

    for s in skills:
        if isinstance(s, str):
            clean.append(s.lower().strip())

        elif isinstance(s, dict):
            name = s.get("name")
            if name:
                clean.append(name.lower().strip())

    return clean


# ---------------------------
# CAREER CLEANING
# ---------------------------
def extract_companies(career_history):

    if not isinstance(career_history, list):
        return []

    companies = []

    for job in career_history:
        if isinstance(job, dict):
            company = job.get("company")
            if company:
                companies.append(company)

    return companies


# ---------------------------
# MAIN EXTRACTOR
# ---------------------------
def extract_candidate(raw):

    if not isinstance(raw, dict):
        return None

    profile = raw.get("profile", {})

    candidate = {
        "candidate_id": raw.get("candidate_id", ""),
        "name": extract_name(raw),

        # profile text signals
        "headline": safe_get(profile, "headline", ""),
        "summary": safe_get(profile, "summary", ""),

        # structured data
        "skills": extract_skills(raw.get("skills", [])),
        "companies": extract_companies(raw.get("career_history", [])),

        "experience": safe_get(profile, "years_of_experience", 0),

        "education": raw.get("education", []),

        # important signals
        "redrob_signals": raw.get("redrob_signals", {})
    }

    return candidate