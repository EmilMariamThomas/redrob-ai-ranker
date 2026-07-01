def technical_score(candidate):

    skills = candidate.get("skills", [])

    if not isinstance(skills, list):
        return 0

    score = 0

    strong_skills = {
        "python", "ml", "machine learning", "ai", "deep learning",
        "nlp", "pytorch", "tensorflow", "docker", "kubernetes",
        "aws", "gcp", "azure", "flask", "fastapi", "spark"
    }

    for skill in skills:

        # CASE 1: dict format {"name": "NLP"}
        if isinstance(skill, dict):
            name = skill.get("name", "").lower()

        # CASE 2: string format "NLP"
        elif isinstance(skill, str):
            name = skill.lower()

        else:
            continue

        if name in strong_skills:
            score += 10
        else:
            score += 3

    return min(score, 100)