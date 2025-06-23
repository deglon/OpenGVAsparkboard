from llm_agent import call_groq

# Example prompt to test OpenAI (or Groq if you prefer)
prompt = "Summarize the following review: 'This tool is highly relevant for clinical workflows, offering evidence-based recommendations.'"

# Test with OpenAI
response = call_groq(prompt)
print("Groq Response:", response)
