def safe_text_list(items):

    if not isinstance(items, list):
        return ""

    clean = []

    for x in items:
        if isinstance(x, str):
            clean.append(x)

        elif isinstance(x, dict):
            # try common keys
            if "name" in x:
                clean.append(str(x["name"]))
            elif "title" in x:
                clean.append(str(x["title"]))
            elif "company" in x:
                clean.append(str(x["company"]))

    return " ".join(clean)


def jd_score(candidate):

    text = " ".join([
        str(candidate.get("summary", "")),
        safe_text_list(candidate.get("skills", [])),
        safe_text_list(candidate.get("companies", []))
    ]).lower()

    score = 0

    # -------------------------
    # JD INTENT SIGNALS
    # -------------------------

    if any(x in text for x in ["ranking", "retrieval", "search", "recommendation"]):
        score += 25

    if any(x in text for x in ["embedding", "vector", "similarity", "faiss", "milvus"]):
        score += 20

    if any(x in text for x in ["airflow", "pipeline", "production", "ml system"]):
        score += 15

    if any(x in text for x in ["llm", "fine-tuning", "rag"]):
        score += 10

    # experience boost
    if candidate.get("experience", 0) >= 5:
        score += 10

    # -------------------------
    # BEHAVIOR PENALTY (IMPORTANT JD RULE)
    # -------------------------

    signals = candidate.get("redrob_signals", {})

    if signals.get("recruiter_response_rate", 1) < 0.3:
        score -= 10

    if signals.get("last_active_days", 0) > 180:
        score -= 10

    return min(max(score, 0), 100)