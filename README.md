Here’s your updated `README.md` reflecting:

* The correct course name (Knowledge Organization Systems)
* Your professor and TA
* GitHub context and project identity

---

## ✅ Final `README.md`

````md
# OpenGeneva Sparkboard Feedback Engine

This project simulates an intelligent peer review pipeline for OpenGeneva Sparkboard hackathons.  
It integrates semantic matching, reviewer profiling, and AI-inspired scoring to improve the quality and structure of hackathon feedback.

Developed as part of the **Knowledge Organization Systems** course  
Taught by **Prof. Thomas Maillart**, with **TA Thibaut Chataing**  
University of Geneva, 2025

---

## 🔍 What It Does

- Matches reviewers to projects using an extensible ontology
- Analyzes review quality using simulated LLM logic
- Profiles reviewers via LinkedIn/GitHub or self-rated confidence
- Computes reviewer trust scores across projects
- Filters low-effort or off-topic reviews
- Generates structured, ranked summaries (text + HTML)

---

## 🧠 Core Pipeline

- `data/` → CSVs for projects, reviewers, reviews, and ontology
- `pipeline/` → Modular scripts for scoring, profiling, filtering, summarizing
- `outputs/` → Feedback summaries, reviewer trust scores, HTML exports
- `run_pipeline.py` → Runs all pipeline steps end-to-end

---

## ⚙️ How to Run

```bash
python run_pipeline.py
````

Pipeline Steps:

1. Score reviews and match domains
2. Profile reviewers
3. Rank feedback
4. Interpret using AI-style logic
5. Generate summaries (text + HTML)
6. Output reviewer trust scores

---

## 🗂 Example Outputs

* `data/scored_reviews.csv`
* `data/profiled_reviews.csv`
* `data/reviewer_trust_score.csv`
* `outputs/feedback_summary_profiled.txt`
* `outputs/html_summaries/` (per project)

---

## 🧪 Ontology

The domain ontology is stored in `data/domain_ontology.json`
It maps concepts like `AI → NLP, Deep Learning`, allowing reviewer-project semantic alignment.

---

## 📦 Requirements

* Python 3.10+
* pandas

Install:

```bash
pip install -r requirements.txt
```

---

## ✍️ Contributors

This system was built by students at the University of Geneva
for the 2025 OpenGeneva event as a real-world extension of Sparkboard peer feedback.

---

## 📌 Future Ideas

* Live Sparkboard integration
* Real LLM API feedback
* Web-based dashboard for review coordination
