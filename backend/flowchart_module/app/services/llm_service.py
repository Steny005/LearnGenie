import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_flowchart_from_llm(user_input: str):

    # Fast prompt for 3-4 steps
    prompt = f"""
FAST FLOWCHART for: {user_input}
3-4 nodes max. JSON only.

Example:
{{
  "nodes": [{{"id":"1","text":"Step 1"}},{{"id":"2","text":"Step 2"}}],
  "edges": [{{"from_node":"1","to_node":"2"}}]
}}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 250, # Fast output
                    "temperature": 0.1,
                    "num_ctx": 1024 # Fast pre-fill
                }
            },
            timeout=58
        )
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        raise Exception(f"Speed Error: Generation took too long (>60s).")