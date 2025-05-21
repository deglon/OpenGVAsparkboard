import subprocess

steps = [
    ("Step 0: Generate reviews using Groq", "python pipeline/groq_generate_reviews.py"),
    ("Step 1: Merge generated reviews", "python pipeline/merge_generated_reviews.py"),
    ("Step 2: Scoring reviews", "python pipeline/review_scoring_pipeline.py"),
    ("Step 3: Profiling reviewers", "python pipeline/reviewer_profiling.py"),
    ("Step 4: Ranking with profiles", "python pipeline/rerank_with_profiles.py"),
    ("Step 5: Generating feedback summary", "python pipeline/generate_feedback_summary.py"),
    ("Step 6: Generate structured summary", "python pipeline/generate_structured_summary.py"),
    ("Step 7: Generate structured HTML", "python pipeline/generate_structured_html.py"),
    ("Step 8: Generate reviewer trust scores", "python pipeline/generate_reviewer_trust.py")
]

print("\n🔁 Running Full Review Feedback Pipeline\n")

for label, command in steps:
    print(f"\n➡️ {label}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Failed at: {label}")
        break
else:
    print("\n✅ All steps completed successfully.")
