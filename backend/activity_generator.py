import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_activity(topic):

    prompt = f"""
Design one innovative classroom activity.

Topic: {topic}

Use memory retention techniques such as:
- retrieval practice
- embodied learning
- visual encoding
- problem-based learning

Return:

Title
Objective
Procedure
Expected Outcome
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]