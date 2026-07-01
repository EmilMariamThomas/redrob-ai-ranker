from utils.technical import technical_score
from utils.career import career_score
from utils.behavior import behavior_score
from utils.jd_intent import jd_score
from utils.reasoning import generate_reason


def compute_final_score(candidate):
    """
    Computes all scores, stores them inside the candidate dictionary,
    generates reasoning, and returns the updated candidate.
    """

    tech = technical_score(candidate)
    career = career_score(candidate)
    behavior = behavior_score(candidate)
    jd = jd_score(candidate)

    final = (
        0.35 * tech +
        0.25 * career +
        0.20 * behavior +
        0.20 * jd
    )

    # Store all scores
    candidate["tech_score"] = tech
    candidate["career_score"] = career
    candidate["behavior_score"] = behavior
    candidate["jd_score"] = jd
    candidate["score"] = round(final, 2)

    # Generate explanation
    candidate["reason"] = generate_reason(candidate)

    # Return the COMPLETE candidate dictionary
    return candidate