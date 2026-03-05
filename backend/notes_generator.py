import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_notes(topic, target_words):

    prompt = f"""
You are an expert educator.

Generate structured classroom teaching notes.

Topic: {topic}

Length: mandatorily {target_words} words.

Structure:

1. Introduction
2. Explanation
3. Key Concepts
4. Examples
5. Summary

Use clear language suitable for teaching.
"""

    response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": target_words
            "temperature": 0.2
        }
    }
)

    result = response.json()

    return result["response"]