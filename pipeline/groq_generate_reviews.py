import pandas as pd
import requests
import json
import time

# === CONFIGURATION ===
GROQ_API_KEY = "Replace with your own API key"  
MODEL = "llama3-70b-8192"  # or use "llama3-8b-8192" if needed
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# === LOAD PROJECTS ===
projects = pd.read_csv("data/projects.csv")

generated_reviews = []

# === GENERATE REVIEWS ===
for _, row in projects.iterrows():
    project_id = row["project_id"]
    title = row["project_title"]
    domain = row["project_domain"]

    prompt = f"""
You are an expert reviewer for a hackathon.
Please evaluate this project titled: '{title}'.
Domains: {domain}

Write a detailed review covering:
1. Feasibility
2. Scalability
3. Ethics

Output as a short paragraph.
"""

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You're an expert hackathon reviewer."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    print(f"Requesting review for {project_id}...")

    response = requests.post(GROQ_URL, headers=HEADERS, data=json.dumps(payload))

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        generated_reviews.append({
            "project_id": project_id,
            "reviewer_id": "groq-llm",
            "review_text": content.strip()
        })
    else:
        print(f"Error for {project_id}: {response.status_code} {response.text}")
        continue

    time.sleep(1.2)  # gentle delay to avoid rate limits

# === SAVE OUTPUT ===
df = pd.DataFrame(generated_reviews)
df.to_csv("data/generated_reviews.csv", index=False)
print("Saved to data/generated_reviews.csv")
