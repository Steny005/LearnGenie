import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def generate_flowchart_from_llm(user_input: str):

    # Prompt for flowchart generation
    prompt = f"""
Create a simple learning FLOWCHART for: {user_input}

Rules:
- Return ONLY valid JSON
- 5 nodes minimum
- Node text must describe a real step (not numbers like "1", "2", "3")
- Each step should contain 3-6 words
- No explanations outside JSON

Format exactly like this but can extend upto minimum 5 nodes :

{{
  "nodes":[
    {{"id":"1","text":"First concept"}},
    {{"id":"2","text":"Second concept"}},
    {{"id":"3","text":"Third concept"}},
    {{"id":"4","text":"Fourth concept"}}
  ],
  "edges":[
    {{"from_node":"1","to_node":"2"}},
    {{"from_node":"2","to_node":"3"}},
    {{"from_node":"3","to_node":"4"}}
  ]
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
                    "num_predict": 250,
                    "temperature": 0.1,
                    "num_ctx": 1024
                }
            },
            timeout=45
        )

        response.raise_for_status()
        result = response.json()
        return result["response"]

    except requests.exceptions.RequestException:
        raise Exception("Speed Error: Generation took too long (>60s).")