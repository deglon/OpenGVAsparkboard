# This script is a fallback simulator for structured review scoring
# Use only if you're not calling real LLMs (like Groq or OpenAI)


import pandas as pd
import random

# Load scored reviews
df = pd.read_csv("data/scored_reviews.csv")

# Simulated LLM output function
def fake_llm_review_analysis(review_text):
    # Simple heuristic based on keywords
    text = review_text.lower()

    def keyword_score(words):
        return min(5, sum(kw in text for kw in words) + random.choice([0, 1]))

    return {
        "feasibility_score": keyword_score(["feasibility", "realistic", "workable"]),
        "scalability_score": keyword_score(["scale", "scalable", "expansion"]),
        "ethics_score": keyword_score(["ethics", "privacy", "bias", "transparency"]),
        "llm_comment": f"Simulated response based on: '{review_text[:40]}...'"
    }

# Apply the simulation to each review
expanded_data = df.copy()

scores = expanded_data["review_text"].apply(fake_llm_review_analysis).apply(pd.Series)
expanded_data = pd.concat([expanded_data, scores], axis=1)

# Save the new structured review dataset
expanded_data.to_csv("data/structured_reviews.csv", index=False)
print("AI interpretation complete. Results saved to structured_reviews.csv")
