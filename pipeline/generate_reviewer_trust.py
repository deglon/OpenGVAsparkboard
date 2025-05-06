import pandas as pd

# Load structured review data
df = pd.read_csv("data/structured_reviews.csv")

# Group by reviewer
reviewer_stats = df.groupby("reviewer_id").agg({
    "domain_relevance": "mean",
    "feasibility_score": "mean",
    "scalability_score": "mean",
    "ethics_score": "mean"
}).reset_index()

# Add composite trust score
def compute_trust(row):
    base = (
        row["feasibility_score"] +
        row["scalability_score"] +
        row["ethics_score"]
    ) / 3
    return round(base * row["domain_relevance"], 2)

reviewer_stats["trust_score"] = reviewer_stats.apply(compute_trust, axis=1)

# Save results
reviewer_stats.to_csv("data/reviewer_trust_score.csv", index=False)
print("Reviewer trust scores saved to data/reviewer_trust_score.csv")
