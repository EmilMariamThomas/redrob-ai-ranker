def generate_reason(candidate):
    profile = candidate.get("profile", {})

    name = profile.get("anonymized_name", "Unknown")
    years = profile.get("years_of_experience", 0)
    title = profile.get("current_title", "")
    skills = profile.get("skills", [])
    signals = candidate.get("redrob_signals", {})

    reasons = []

    # EXPERIENCE SIGNAL
    if years >= 6:
        reasons.append("Strong industry experience")
    elif years >= 3:
        reasons.append("Moderate industry experience")
    else:
        reasons.append("Early career profile")

    # TECH SIGNAL
    skill_names = []
    if isinstance(skills, list):
        for s in skills:
            if isinstance(s, dict):
                skill_names.append(s.get("name", ""))
            elif isinstance(s, str):
                skill_names.append(s)

    skill_text = " ".join(skill_names).lower()

    if any(x in skill_text for x in ["ml", "ai", "spark", "nlp", "pytorch", "tensorflow"]):
        reasons.append("Strong ML/AI skill alignment")

    if any(x in skill_text for x in ["sql", "python", "airflow", "kafka"]):
        reasons.append("Strong data engineering background")

    # BEHAVIOR SIGNAL
    if signals.get("recruiter_response_rate", 0) > 0.7:
        reasons.append("High recruiter engagement")
    elif signals.get("recruiter_response_rate", 0) > 0.4:
        reasons.append("Moderate recruiter engagement")
    else:
        reasons.append("Low recruiter responsiveness")

    # JOB READINESS
    if signals.get("open_to_work_flag"):
        reasons.append("Actively open to work")

    if signals.get("interview_completion_rate", 0) > 0.7:
        reasons.append("Reliable interview participation")

    # FINAL COMBINE (IMPORTANT FOR JD STORY)
    if len(reasons) == 0:
        reasons.append("General candidate profile")

    return "; ".join(reasons[:3])