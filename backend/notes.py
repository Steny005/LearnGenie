import requests
def generate_notes(topic: str, content: str, target_words: int):
    prompt = f"""
You are an expert educator tasked with creating concise and effective notes for the topic '{topic}'
The notes must:
-be approximately {target_words} words in length
-be well structured with clear headings and subheadings
- Include explanation, examples, and summary
- Avoid unnecessary repetition
- Focus on the provided content {content}  and go beyond it. we need structured, most precise correct notes on the {topic}
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
    generated_text = result.get("response","")

    return{
        "title": topic,
        "estimated_word_count": target_words,
        "content": generated_text
    } 