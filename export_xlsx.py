import pandas as pd


def export_xlsx(candidates, path="output/submission.xlsx"):

    rows = []

    for rank, c in enumerate(candidates, start=1):

        profile = c.get("profile", {})

        name = (
            profile.get("anonymized_name")
            or profile.get("name")
            or "Unknown"
        )

        rows.append({
            "Rank": rank,
            "Candidate ID": c.get("candidate_id"),
            "Name": name,
            "Final Score": round(c.get("score", 0), 2),
            "Tech Score": c.get("tech_score", 0),
            "Career Score": c.get("career_score", 0),
            "Behavior Score": c.get("behavior_score", 0),
            "Reason": c.get("reason", "")
        })

    df = pd.DataFrame(rows)

    df.to_excel(path, index=False)

    print(f"✅ Excel saved at: {path}")