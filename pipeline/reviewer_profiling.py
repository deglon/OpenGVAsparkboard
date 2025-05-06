import pandas as pd

df = pd.read_csv("data/scored_reviews.csv")
reviewers = pd.read_csv("data/reviewers.csv")

# Merge to get access to profile info and confidence
merged = df.merge(reviewers[["reviewer_id", "linkedin", "github", "confidence_score"]], on="reviewer_id", how="left")

# Function to decide expertise score
def get_expertise_score(row):
    has_profile = pd.notna(row["linkedin"]) or pd.notna(row["github"])
    if has_profile:
        # Trust domain_relevance (based on their declared domains)
        return row["domain_relevance"]
    else:
        # Fallback to self-reported confidence
        return float(row["confidence_score"]) if not pd.isna(row["confidence_score"]) else 0.0

# Apply expertise scoring
merged["expertise_score"] = merged.apply(get_expertise_score, axis=1)

# combine expertise with review_score
merged["final_weighted_score"] = (
    merged["review_score"] * 0.7 +
    merged["expertise_score"] * 3
)

# Save
merged.to_csv("data/profiled_reviews.csv", index=False)
print("Reviewer profiling complete. Saved to profiled_reviews.csv")
