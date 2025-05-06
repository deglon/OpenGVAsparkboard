import pandas as pd
import json

# Load CSV files
projects = pd.read_csv("data/projects.csv")
reviewers = pd.read_csv("data/reviewers.csv")
reviews = pd.read_csv("data/reviews.csv")

# Merge the data
merged = reviews.merge(projects, on="project_id").merge(reviewers, on="reviewer_id")

# Load ontology
with open("data/domain_ontology.json") as f:
    ontology = json.load(f)

# Expand function using ontology
def expand_domains(domains):
    expanded = set()
    for domain in domains.split(','):
        domain = domain.strip().lower()
        expanded.add(domain)
        expanded.update(ontology.get(domain, []))
    return expanded

# Ontology match + return matched terms
def domain_match_terms(project_domains, reviewer_domains):
    proj_set = expand_domains(project_domains)
    rev_set = expand_domains(reviewer_domains)
    matched = proj_set & rev_set
    relevance = len(matched) / len(proj_set) if proj_set else 0.0
    return relevance, ", ".join(sorted(matched)) if matched else "None"

# Keyword-based review scoring
def review_score(text):
    keywords = [
        'feasibility', 'scalability', 'ethics',
        'impact', 'privacy', 'objectives', 'governance'
    ]
    return sum(kw in text.lower() for kw in keywords)

# Apply all scoring
merged["review_score"] = merged["review_text"].apply(review_score)

# Apply domain matching with term tracking
merged[["domain_relevance", "matched_terms"]] = merged.apply(
    lambda row: pd.Series(domain_match_terms(row["project_domain"], row["reviewer_domains"])),
    axis=1
)

# Output final scored review file
output = merged[[
    "project_id", "reviewer_id", "review_text", "review_score",
    "domain_relevance", "matched_terms"
]]

output.to_csv("data/scored_reviews.csv", index=False)
print("Scoring complete. Results saved to scored_reviews.csv")
