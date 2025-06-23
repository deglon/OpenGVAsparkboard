import pandas as pd

# Load human reviews
human_reviews = pd.read_csv("data/reviews.csv")
human_reviews["review_type"] = "human"

# Load Groq-generated reviews
groq_reviews = pd.read_csv("data/generated_reviews.csv")
groq_reviews["review_type"] = "groq-llm"

# Combine and deduplicate
combined = pd.concat([human_reviews, groq_reviews], ignore_index=True).drop_duplicates(
    subset=["project_id", "reviewer_id", "review_text"]
)

# Save back to the same file
combined.to_csv("data/reviews.csv", index=False)
print(f"Merged reviews saved to data/reviews.csv — total: {len(combined)} rows.")
