from utils.scorer import compute_final_score


def rank_candidates(candidates):
    """
    Score every candidate and sort by:
    1. Higher score first
    2. Lower candidate_id first (tie-break)
    """

    ranked = []

    for candidate in candidates:
        ranked.append(compute_final_score(candidate))

    ranked.sort(
        key=lambda c: (
            -c["score"],
            c["candidate_id"]
        )
    )

    return ranked