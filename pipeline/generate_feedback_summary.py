import pandas as pd

# Load ranked reviews using profiled scores
df = pd.read_csv("data/ranked_reviews_profiled.csv")

# Load reviewer trust scores
trust_df = pd.read_csv("data/reviewer_trust_score.csv")

# Merge trust scores and reviews
df = df.merge(trust_df[["reviewer_id", "trust_score"]], on="reviewer_id", how="left")

# Sort and select top 3 reviewers
top_reviewers = trust_df.sort_values(by="trust_score", ascending=False).head(3)

# Start summary
summaries = []

summaries.append("Top 3 Most Trusted Reviewers:\n")
for _, row in top_reviewers.iterrows():
    summaries.append(f"- {row['reviewer_id']} (trust score: {round(row['trust_score'], 2)})")
summaries.append("\n" + "=" * 40 + "\n")

# Keywords to detect
keywords = ['feasibility', 'scalability', 'ethics', 'impact', 'privacy', 'objectives', 'governance']

# Project-level summaries
for project_id, group in df.groupby("project_id"):
    summary = []
    summary.append(f"Project ID: {project_id}")
    summary.append("-" * 40)

    keyword_counts = {kw: 0 for kw in keywords}
    for review in group["review_text"]:
        for kw in keywords:
            if kw in review.lower():
                keyword_counts[kw] += 1

    summary.append("Top Feedback Themes:")
    for kw, count in keyword_counts.items():
        if count > 0:
            summary.append(f"- {kw.capitalize()}: mentioned by {count} reviewer(s)")

    summary.append("\nReviewer Insights (sorted by weighted score):")
    for _, row in group.sort_values(by="final_weighted_score", ascending=False).iterrows():
        reviewer_id = row["reviewer_id"]
        score = round(row["final_weighted_score"], 2)
        trust = round(row["trust_score"], 2)
        matched = row.get("matched_terms", "None")
        comment = row["review_text"]
        summary.append(f"- {reviewer_id} (score: {score}, trust: {trust}, match: {matched}): \"{comment}\"")

    summary.append("\n")
    summaries.append("\n".join(summary))

# Write to output
with open("output/feedback_summary_profiled.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(summaries))

print("Full profiled feedback summary with trust scores and matched terms saved to outputs/feedback_summary_profiled.txt")
