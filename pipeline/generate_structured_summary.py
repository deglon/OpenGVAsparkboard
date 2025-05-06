import pandas as pd

# Load structured AI-enhanced review data
df = pd.read_csv("data/structured_reviews.csv")

# Output holder
summaries = []

# Group by project
for project_id, group in df.groupby("project_id"):
    summary = []
    summary.append(f"Project ID: {project_id}")
    summary.append("-" * 40)

    # Compute averages
    avg_feasibility = round(group["feasibility_score"].mean(), 2)
    avg_scalability = round(group["scalability_score"].mean(), 2)
    avg_ethics = round(group["ethics_score"].mean(), 2)

    summary.append("Average Scores:")
    summary.append(f"- Feasibility: {avg_feasibility}/5")
    summary.append(f"- Scalability: {avg_scalability}/5")
    summary.append(f"- Ethics: {avg_ethics}/5")

    # Sample insights
    summary.append("\nLLM Comments from Reviewers:")
    for _, row in group.iterrows():
        summary.append(f"- Reviewer {row['reviewer_id']}: {row['llm_comment']}")

    summary.append("\n")
    summaries.append("\n".join(summary))

# Save summary to file
with open("output/structured_feedback_summary.txt", "w") as f:
    f.write("\n".join(summaries))

print("Structured feedback summary saved to outputs/structured_feedback_summary.txt")
