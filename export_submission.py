import csv

def export_submission(ranked_candidates, output_path="output/submission.csv"):
    """
    Creates final hackathon CSV in required format:
    candidate_id,rank,score,reasoning
    """

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # header (MANDATORY ORDER)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])

        for i, c in enumerate(ranked_candidates[:100]):
            candidate_id = c.get("candidate_id", "")

            # safety fallback
            if not candidate_id:
                continue

            score = round(float(c.get("score", 0)), 4)

            reasoning = c.get("reason", "")

            # enforce 1–2 sentence limit (basic cleanup)
            reasoning = ". ".join(reasoning.split(".")[:2]).strip()

            writer.writerow([
                candidate_id,
                i + 1,
                score,
                reasoning
            ])

    print(f"\n📦 Submission CSV saved at: {output_path}")