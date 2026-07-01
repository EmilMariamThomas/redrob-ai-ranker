def career_score(candidate):

    # SAFE GET (prevents KeyError)
    career_history = candidate.get("career_history") or candidate.get("companies") or []

    if not isinstance(career_history, list):
        career_history = []

    score = 0

    big_companies = ["google", "amazon", "microsoft", "meta", "apple", "netflix"]

    # experience quality
    score += min(len(career_history) * 5, 20)

    for job in career_history:
        job = str(job).lower()

        if any(b in job for b in big_companies):
            score += 10

        if "senior" in job or "lead" in job:
            score += 5

    return min(score, 100)