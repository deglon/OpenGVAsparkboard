## ✅ `README.md`

````md
# OpenGeneva Sparkboard Feedback Engine

This project simulates an intelligent peer review pipeline for OpenGeneva Sparkboard hackathons.  
It matches reviewers to projects using an ontology, profiles expertise, scores reviews using Groq's LLM, and generates structured feedback with reviewer trust scores.

Built during the **Knowledge Organization Systems** course at the University of Geneva, 2025  
**Prof. Thomas Maillart** · **TA Thibaut Chataing**

---

## 🔍 What It Does

- Matches reviewers to projects using ontology-based domain expansion
- Generates reviews with Groq (LLaMA-3) for each project
- Merges LLM-generated reviews with human feedback
- Scores reviews and ranks them by relevance + content quality
- Computes reviewer trust scores from multiple signals
- Produces clear feedback summaries (TXT + HTML)

---

## 🧠 Core Pipeline Steps

```bash
python run_pipeline.py
````

This script executes:

1. Generate Groq reviews (`groq_generate_reviews.py`)
2. Merge LLM and human reviews (`merge_generated_reviews.py`)
3. Score reviews + domain alignment (`review_scoring_pipeline.py`)
4. Profile reviewers (`reviewer_profiling.py`)
5. Rank reviews (`rerank_with_profiles.py`)
6. Generate text summaries (`generate_feedback_summary.py`)
7. Generate structured summaries (`generate_structured_summary.py`)
8. Export per-project HTML summaries (`generate_structured_html.py`)
9. Calculate reviewer trust scores (`generate_reviewer_trust.py`)

---

## 🗂 Project Structure

```
OpenGVAsparkboard/
├── data/
│   ├── projects.csv
│   ├── reviewers.csv
│   ├── reviews.csv
│   ├── generated_reviews.csv
│   ├── structured_reviews.csv
│   └── reviewer_trust_score.csv
├── outputs/
│   ├── feedback_summary_profiled.txt
│   └── html_summaries/
├── pipeline/
│   └── [all processing scripts]
└── run_pipeline.py
```

---

## ✨ Example Outputs

* `feedback_summary_profiled.txt` – human + LLM feedback by project
* `structured_reviews.csv` – feasibility, ethics, scalability scores
* `reviewer_trust_score.csv` – ranked trust per reviewer
* `html_summaries/` – clean per-project summaries for publishing

---

## 🧪 Ontology

Stored in `data/domain_ontology.json`, used to:

* Expand reviewer/project domains
* Detect mismatches
* Improve domain relevance scoring

---

## 🧰 Requirements

```bash
pip install pandas requests
```

---

## 📦 Future Extensions

<<<<<<< release/final-pipeline
* Live integration with Sparkboard API
* Use OpenAI or Claude for multi-model scoring
* Add a dashboard for reviewers and teams
* Real-time review ingestion and scoring during hackathons
=======
This system was built by students (Oussama Rattazi, Mahidhar Reddy Vaka) at the University of Geneva
for the 2025 OpenGeneva event as a real-world extension of Sparkboard peer feedback.
>>>>>>> main

---

## 🧑‍💻 Authors

Developed by students at the University of Geneva
Course: Knowledge Organization Systems · Spring 2025
