import json
import gzip


def load_candidates(path):
    candidates = []

    # open file safely (.jsonl or .jsonl.gz)
    if path.endswith(".gz"):
        f = gzip.open(path, "rt", encoding="utf-8")
    else:
        f = open(path, "r", encoding="utf-8")

    for line in f:
        if not line.strip():
            continue

        obj = json.loads(line)

        # ===============================
        # 🔥 FIX: ALWAYS FLATTEN NAME
        # ===============================
        profile = obj.get("profile", {})

        obj["name"] = profile.get("anonymized_name") or "Unknown"

        # optional safety fields (avoid KeyErrors later)
        obj["tech_score"] = obj.get("tech_score", 0)
        obj["career_score"] = obj.get("career_score", 0)
        obj["behavior_score"] = obj.get("behavior_score", 0)

        candidates.append(obj)

    f.close()
    return candidates