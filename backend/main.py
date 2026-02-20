from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

from time_alloc import calculate_time_distribution
from generate import generate_content
from notes import format_notes

app = FastAPI()

DEFAULT_DURATION = 45

class LessonInput(BaseModel):
    topic: str
    description: Optional[str] = ""
    duration_minutes: Optional[int] = None


@app.post("/generate")
def generate_lesson(data: LessonInput):

    # 1️⃣ Handle default duration safely
    duration = data.duration_minutes or DEFAULT_DURATION

    # 2️⃣ Calculate structured time distribution
    time_data = calculate_time_distribution(duration)

    # 3️⃣ Call unified generator (Single AI call)
    raw_output = generate_content(
        topic=data.topic,
        description=data.description,
        target_words=time_data["target_words"]
    )

    # 4️⃣ Parse JSON safely
    try:
        parsed = json.loads(raw_output)
    except Exception:
        return {
            "error": "Model did not return valid JSON",
            "raw_output": raw_output
        }

    # 5️⃣ Return structured response
    return {
        "topic": data.topic,
        "total_duration": time_data["total_duration"],
        "time_distribution": {
            "intro": time_data["intro"],
            "explanation": time_data["explanation"],
            "examples": time_data["examples"],
            "activities": time_data["activities"],
            "recap": time_data["recap"]
        },
        "notes": parsed.get("notes"),
        "flowchart": parsed.get("flowchart"),
        "activity": parsed.get("activity")
    }