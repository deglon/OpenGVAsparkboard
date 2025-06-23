import requests

# --- HARDCODE YOUR GROQ API KEY AND ENDPOINT HERE ---
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq(prompt, model="llama-3.3-70b-versatile"):
    """Call Groq's chat completion API with a prompt."""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

# Example usage:
# response = call_groq("Summarize this review: ...", model="llama-3.3-70b-versatile")