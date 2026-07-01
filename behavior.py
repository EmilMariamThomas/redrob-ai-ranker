def behavior_score(candidate):

    signals = candidate["redrob_signals"]

    score = 0

    if signals["open_to_work_flag"]:
        score += 4

    if signals["recruiter_response_rate"] >= 0.80:
        score += 4
    elif signals["recruiter_response_rate"] >= 0.60:
        score += 3
    elif signals["recruiter_response_rate"] >= 0.40:
        score += 2

    if signals["interview_completion_rate"] >= 0.80:
        score += 3

    if signals["github_activity_score"] >= 70:
        score += 3
    elif signals["github_activity_score"] >= 40:
        score += 2
    elif signals["github_activity_score"] >= 10:
        score += 1

    if signals["willing_to_relocate"]:
        score += 2

    if signals["notice_period_days"] <= 30:
        score += 2
    elif signals["notice_period_days"] <= 60:
        score += 1

    if signals["verified_email"]:
        score += 1

    if signals["verified_phone"]:
        score += 1

    return (min(score, 20) / 20) * 100