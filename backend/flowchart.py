import requests
def generate_flowchart(topic: str):
    prompt = f"""
You are an expert systems educator.

Generate a flowchart representation for the topic: "{topic}".

Rules:
- Show cause → process → decision → outcome progression.
- Include logical dependencies.
- If relevant, include decision points (Yes/No branches).
- Avoid generic words like "Introduction".
- Each node must be a meaningful process step.
- Output in arrow-based format.
- No explanation text.

Format example:

Start → Resource Request → Resource Allocation Check  
If Available → Allocate Resource → Continue Execution  
If Not Available → Add to Wait Queue → Check for Circular Wait  
Circular Wait Detected → Deadlock State  
No Circular Wait → Resume Execution  
End

Now generate the structured flowchart for:
{topic}
"""
    response = requests.post(
         "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
        >
    )
 

