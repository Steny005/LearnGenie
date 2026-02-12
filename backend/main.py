from fastapi import FastAPI
from normalizer import CoreInput
from time_alloc import calculate_time_distribution
from lessonplanner import generate_lesson_plan
from flowchart import generate_flowchart
from activity import generate_activities
from notes import generate_notes
app = FastAPI()

from normalizer import GenerateResponse
@app.post("/generate", response_model=GenerateResponse)

def generate(content: CoreInput):

    time_data = calculate_time_distribution(content.duration_minutes)

    notes = generate_notes(
        content.topic,
        content.content,
        time_data["target_words"]
    )

    flowchart = generate_flowchart(content.topic) if content.include_flowchart else None
    activities = generate_activities(content.topic) if content.include_activities else None
    lesson_plan = generate_lesson_plan(content.duration_minutes, time_data) if content.include_lesson_plan else None

    return {
        "notes": notes,
        "flowchart": flowchart,
        "activities": activities,
        "lesson_plan": lesson_plan
    }
