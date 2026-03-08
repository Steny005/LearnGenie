import re
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def clean_text(text):
    """Remove formatting noise from pasted text or PDFs"""

    text = text.replace("\n", " ")

    # remove sources like IBM +2
    text = re.sub(r"\b[A-Z]{2,}\b(\s*\+\d+)?", "", text)

    # remove bullet characters
    text = re.sub(r"[•●\-]", " ", text)

    # collapse spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_text(text, chunk_size=1000):
    """Split long text into smaller pieces"""

    text = text.replace("\n", " ").strip()

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def summarize_chunk(text):
    """Summarize one chunk"""

    prompt = f"""
Summarize the following text into a short topic description.

Rules:
- Maximum 40 words
- Focus on the main concept only
- Remove statistics and formatting

Text:
{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 70,
                "temperature": 0.2,
                "num_ctx": 768
            }
        },
        timeout=40
    )

    response.raise_for_status()

    return response.json()["response"]


def summarize_long_text(text):
    """Full pipeline: clean → chunk → summarize"""

    text = clean_text(text)

    # prevent extremely large prompts
    text = text[:3000]

    chunks = split_text(text)

    summaries = []

    for chunk in chunks:
        summary = summarize_chunk(chunk)
        summaries.append(summary)

    combined_summary = " ".join(summaries)

    return combined_summary 