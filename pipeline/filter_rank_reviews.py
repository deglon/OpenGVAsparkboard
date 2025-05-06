import pandas as pd

# Load the scored reviews
df = pd.read_csv("data/scored_reviews.csv")

# Thresholds
REVIEW_SCORE_THRESHOLD = 2
DOMAIN_RELEVANCE_THRESHOLD = 0.5

# Filter out weak reviews
filtered = df[
    (df["review_score"] >= REVIEW_SCORE_THRESHOLD) &
    (df["domain_relevance"] >= DOMAIN_RELEVANCE_THRESHOLD)
].copy()

# Calculate combined score
filtered["combined_score"] = (
    filtered["review_score"] * 0.7 +
    filtered["domain_relevance"] * 3
)

# Sort reviews per project by usefulness
ranked = filtered.sort_values(
    by=["project_id", "combined_score"],
    ascending=[True, False]
)

# Save result
ranked.to_csv("data/ranked_reviews.csv", index=False)
print("Ranking complete. Results saved to ranked_reviews.csv")
