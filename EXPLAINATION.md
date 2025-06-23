# Project Pipeline Explanation

This document explains how the OpenGeneva Sparkboard Feedback Engine works.

---

## 🧠 What the System Does

It simulates a peer review process for hackathons using:

- Reviewer-project domain matching (via ontology)
- Human and LLM-generated reviews
- Scoring, filtering, and ranking of feedback
- Trust score calculation for reviewers
- Structured feedback summaries (text + HTML)

---

## 🔁 Pipeline Breakdown

### Step 0: Generate Reviews with Groq
Uses Groq's LLaMA-3 to generate artificial reviews for every project.
- Input: `projects.csv`
- Output: `generated_reviews.csv`

### Step 1: Merge Reviews
Combines human-written reviews with Groq-generated ones.
- Adds a `review_type` column
- Output: updated `reviews.csv`

### Step 2: Score Reviews + Match Domains
Calculates:
- `review_score` → keyword-based quality
- `domain_relevance` → semantic match using ontology
- Output: `scored_reviews.csv`

### Step 3: Profile Reviewers
Adds expertise using:
- LinkedIn/GitHub links
- or fallback confidence score
- Combines with review score to compute `final_weighted_score`
- Output: `profiled_reviews.csv`

### Step 4: Rank Reviews
Filters out weak feedback and ranks the rest by final score.
- Output: `ranked_reviews_profiled.csv`

### Step 5: Feedback Summary (Text)
Generates per-project summaries:
- Top feedback themes (feasibility, ethics, etc.)
- Each reviewer’s comment, score, and trust
- Output: `feedback_summary_profiled.txt`

### Step 6: Structured Score Summary
Averages LLM scores per project.
- Output: `structured_feedback_summary.txt`

### Step 7: HTML Summaries
Visual feedback per project.
- Output: `html_summaries/P1.html`, etc.

### Step 8: Reviewer Trust Scores
Calculates trust for each reviewer based on:
- Domain relevance
- Feasibility / ethics / scalability scoring
- Output: `reviewer_trust_score.csv`

---

## 🔄 Everything Runs with:
```bash
python run_pipeline.py

📁 Outputs You Can Trust
reviews.csv → complete with human + Groq feedback

scored_reviews.csv → includes domain matches

structured_reviews.csv → adds feasibility/ethics scoring

feedback_summary_profiled.txt → clean summaries to give back to teams

reviewer_trust_score.csv → shows who gave the most helpful feedback

🛠 For Real Use
This system can be plugged into Sparkboard or any review platform for:

Hackathon feedback

Research peer reviews

Internal innovation evaluations