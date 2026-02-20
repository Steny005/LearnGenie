import requests

def generate_content(topic: str, description: str, target_words: int):

    context_section = f"\nAdditional context to include in notes:\n{description}\n" if description else ""

    prompt = f"""
You are an expert educator.

Generate the following for topic: "{topic}"

{context_section}

1. Structured Notes (~{target_words} words)
   - Must clearly incorporate the additional context if provided.
   - Expand beyond it academically.

2. Logical flowchart (arrow-based)

3. ONE innovative classroom activity.

Return STRICT JSON:
{{
  "notes": "...",
  "flowchart": "...",
  "activity": {{
      "title": "...",
      "objective": "...",
      "procedure": "...",
      "expected_outcome": "..."
  }}
}}
Return only JSON.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result.get("response", "")