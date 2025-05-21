import pandas as pd
import os

# Load AI-enhanced structured reviews
df = pd.read_csv("data/structured_reviews.csv")

# Create output folder
output_dir = "outputs/html_summaries"
os.makedirs(output_dir, exist_ok=True)

# For each project, generate an HTML summary
for project_id, group in df.groupby("project_id"):
    html = []

    html.append(f"<h2>Project {project_id} – Structured Feedback Summary</h2>")
    html.append("<hr>")

    avg_feasibility = round(group["feasibility_score"].mean(), 2)
    avg_scalability = round(group["scalability_score"].mean(), 2)
    avg_ethics = round(group["ethics_score"].mean(), 2)

    html.append("<h3>Average Scores</h3>")
    html.append("<ul>")
    html.append(f"<li><strong>Feasibility</strong>: {avg_feasibility}/5</li>")
    html.append(f"<li><strong>Scalability</strong>: {avg_scalability}/5</li>")
    html.append(f"<li><strong>Ethics</strong>: {avg_ethics}/5</li>")
    html.append("</ul>")

    html.append("<h3>Reviewer Comments</h3>")
    for _, row in group.iterrows():
        html.append(f"<p><strong>Reviewer {row['reviewer_id']}</strong>: {row['review_text']}</p>")

    # Save each project file
    with open(f"{output_dir}/{project_id}.html", "w", encoding="utf-8") as f:
        f.write("\n".join(html))

print(f"Generated HTML summaries in {output_dir}")
