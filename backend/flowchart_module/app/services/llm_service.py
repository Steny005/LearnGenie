import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_flowchart_from_llm(user_input: str):

    prompt = f"""
You convert text into structured flowcharts.

Input:
{user_input}

Instructions:
- If input is just a topic, infer logical steps.
- If it is a paragraph, extract process steps.
- Add decision nodes if needed.
- Return ONLY valid JSON.

Format:
{{
  "nodes": [
    {{"id":"A","text":"Start"}},
    {{"id":"B","text":"Process"}}
  ],
  "edges": [
    {{"from_node":"A","to_node":"B"}}
  ]
}}
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