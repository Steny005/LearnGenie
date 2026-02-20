import re

def format_notes(topic: str, raw_notes: str, duration: int):

    if not raw_notes:
        return {
            "title": topic,
            "summary": "",
            "sections": [],
            "duration_minutes": duration
        }

    # 1️⃣ Extract first sentence as summary
    sentences = raw_notes.split(".")
    summary = sentences[0].strip() + "." if sentences else ""

    # 2️⃣ Detect headings (## or bold or uppercase lines)
    sections = []
    current_heading = "Introduction"
    current_content = []

    lines = raw_notes.split("\n")

    for line in lines:
        stripped = line.strip()

        # Detect markdown headings like ## Heading
        if stripped.startswith("#"):
            # Save previous section
            if current_content:
                sections.append({
                    "heading": current_heading,
                    "content": " ".join(current_content).strip()
                })
                current_content = []

            current_heading = stripped.replace("#", "").strip()

        # Detect bold headings like **Heading**
        elif re.match(r"\*\*(.*?)\*\*", stripped):
            if current_content:
                sections.append({
                    "heading": current_heading,
                    "content": " ".join(current_content).strip()
                })
                current_content = []

            current_heading = stripped.replace("*", "").strip()

        else:
            if stripped:
                current_content.append(stripped)

    # Append last section
    if current_content:
        sections.append({
            "heading": current_heading,
            "content": " ".join(current_content).strip()
        })

    # 3️⃣ Estimate reading time (200 words per minute)
    word_count = len(raw_notes.split())
    read_time = max(1, round(word_count / 200))

    return {
        "title": topic,
        "summary": summary,
        "sections": sections,
        "estimated_read_time_minutes": read_time,
        "duration_minutes": duration,
        "word_count": word_count
    }