# OpenGeneva Sparkboard Feedback Engine

This project simulates an intelligent peer review pipeline for OpenGeneva Sparkboard hackathons.  
It integrates semantic matching, AI-style analysis, and reviewer trust scoring to evaluate feedback quality and relevance.

Built during the Digital Systems and Services Master's at the University of Geneva.

---

## 🔍 What It Does

- ✅ Matches reviewers to projects using domain ontologies
- ✅ Scores review quality with AI-inspired logic
- ✅ Profiles reviewers (using LinkedIn/GitHub or self-rated confidence)
- ✅ Calculates reviewer trust scores
- ✅ Filters low-effort feedback
- ✅ Generates structured summaries in text and HTML

---

## 🧠 Core Components

- `data/`  
  Raw inputs and processed CSVs (`projects.csv`, `reviewers.csv`, `reviews.csv`)

- `pipeline/`  
  Modular scripts for each step of the review analysis pipeline

- `outputs/`  
  Generated summaries and reports

---

## ⚙️ Run the Pipeline

From the project root:

```bash
python run_pipeline.py
