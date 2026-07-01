import json
from utils.loader import load_candidates
from utils.ranking import rank_candidates

DATA_PATH = "data/candidates.jsonl"
OUTPUT_PATH_JSON = "output/submission.json"
OUTPUT_PATH_CSV = "output/submission.csv"


def main():
    print("\n🚀 Loading candidates...")

    candidates = load_candidates(DATA_PATH)

    print(f"✅ Loaded: {len(candidates)} candidates")

    print("\n🧠 Ranking candidates...")

    ranked = rank_candidates(candidates)

    print("✅ Ranking completed")

    print("\n🧠 Adding reasoning layer...\n")

    # Ensure reason exists (safety fallback)
    for c in ranked:
        if "reason" not in c or not c["reason"]:
            c["reason"] = "Balanced technical, career and behavioral fit"

    print("\n🏆 Top 5 Candidates:\n")

    for i, c in enumerate(ranked[:5], start=1):

        profile = c.get("profile", {})

        # FIX NAME ISSUE
        name = (
            profile.get("anonymized_name")
            or profile.get("name")
            or c.get("candidate_id")
            or "Unknown"
        )

        print(f"\n🏆 Rank {i}")
        print(f"Name: {name}")
        print(f"Score: {round(c.get('score', 0), 2)}")
        print(f"Tech: {round(c.get('tech_score', 0), 2)}")
        print(f"Career: {round(c.get('career_score', 0), 2)}")
        print(f"Behavior: {round(c.get('behavior_score', 0), 2)}")
        print(f"Reason: {c.get('reason', 'N/A')}")

    # --------------------------
    # CREATE SUBMISSION FILE
    # --------------------------

    top_100 = ranked[:100]

    # JSON OUTPUT (for debugging)
    with open(OUTPUT_PATH_JSON, "w") as f:
        json.dump(top_100, f, indent=2)

    # CSV OUTPUT (REAL SUBMISSION FORMAT)
    with open(OUTPUT_PATH_CSV, "w") as f:
        f.write("candidate_id,rank,score,reasoning\n")

        for idx, c in enumerate(top_100, start=1):

            cid = c.get("candidate_id", "")
            score = round(c.get("score", 0), 6)
            reason = c.get("reason", "").replace(",", " ")  # CSV safe

            f.write(f"{cid},{idx},{score},\"{reason}\"\n")

    print("\n📦 Submission files generated:")
    print(f"✔ JSON: {OUTPUT_PATH_JSON}")
    print(f"✔ CSV : {OUTPUT_PATH_CSV}")

    print("\n🚀 DONE — READY FOR SUBMISSION")


if __name__ == "__main__":
    main()