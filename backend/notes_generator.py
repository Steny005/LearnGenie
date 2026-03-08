import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_notes(topic, structure):

    target_words = structure["target_words"]

    prompt = f"""
You are an expert teacher preparing structured lesson notes. The notes should be like i can directly read it out from this, so no questions in this, only 
give explanations

Topic: {topic}

Lesson structure (for planning only, DO NOT show durations in output):
Introduction ({structure["intro"]} minutes)
Concept Explanation ({structure["explanation"]} minutes)
Examples ({structure["examples"]} minutes)
Activities ({structure["activities"]} minutes)
Recap ({structure["recap"]} minutes)

Write clean student-friendly notes.

Rules:
- Maximum {target_words} words
- Bullet points preferred
- No markdown symbols (** or ##)
- do not use "**" to mark headings
- No durations in the text
- Use short paragraphs or bullet points
- Clear sections

Structure:

Topic: {topic}

Introduction
Explain the concept clearly in several sentences.

Key Concepts
Explain the main ideas with short explanations.

Examples
Give real-world examples that help understanding.

Activities
Suggest simple learning activities students can do.

Recap
Summarize the key ideas in clear points.
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