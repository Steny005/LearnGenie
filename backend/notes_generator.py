import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_notes(topic, target_words):

    # Extremely concise for speed
    prompt = f"""
EXPERT TEACHING NOTES for: {topic}.
Max {target_words} words. Concise points only.
INTRO, KEY CONCEPTS (3), EXAMPLES (2), SUMMARY.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 350, # Sufficient for notes
                    "temperature": 0.3,
                    "num_ctx": 1024
                }
            },
            timeout=58
        )
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        return f"⚠️ Speed Error: Generation took too long (>60s)."