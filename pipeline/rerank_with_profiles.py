import pandas as pd

# Load the profiled data
df = pd.read_csv("data/profiled_reviews.csv")

# Threshold: final_weighted_score must be at least 2.5 to be considered useful
THRESHOLD = 2.5

# Filter
filtered = df[df["final_weighted_score"] >= THRESHOLD].copy()

# Sort by project + final score
ranked = filtered.sort_values(
    by=["project_id", "final_weighted_score"],
    ascending=[True, False]
)

# Save result
ranked.to_csv("data/ranked_reviews_profiled.csv", index=False)
print("Re-ranking complete. Output saved to ranked_reviews_profiled.csv")
