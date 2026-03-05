import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_activity(topic):

    # Extremely brief for speed
    prompt = f"""
QUICK ACTIVITY for: {topic}.
FORMAT:
- TITLE
- OBJECTIVE (1 line)
- PROCEDURE (3 bullets)
- OUTCOME (1 line)
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 250, # Significantly lower
                    "temperature": 0.4,
                    "num_ctx": 1024
                }
            },
            timeout=58
        )
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        return f"⚠️ Speed Error: Activity generation took too long (>60s)."