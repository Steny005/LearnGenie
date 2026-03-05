from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from notes_generator import generate_notes
from activity_generator import generate_activity
from duration_logic import calculate_target_words

from flowchart_module.app.services.llm_service import generate_flowchart_from_llm
from flowchart_module.app.utils.parser import extract_valid_json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    text: str
    duration: int = 45

def detect_command(text):

    text = text.lower().strip()

    if "@flowchart" in text:
        return text.replace("@flowchart","").strip(), "flowchart"

    if "@activities" in text:
        return text.replace("@activities","").strip(), "activities"

    return text, "notes"

def detect_command(text):

    if "@flowchart" in text:
        return text.replace("@flowchart", "").strip(), "flowchart"

    if "@activities" in text:
        return text.replace("@activities", "").strip(), "activities"

    return text.strip(), "notes"


@app.post("/generate")
def generate(data: UserInput):

    topic, command = detect_command(data.text)

    time_data = calculate_target_words(data.duration)

    if command == "flowchart":

        raw = generate_flowchart_from_llm(topic)
        parsed = extract_valid_json(raw)

        return {"type": "flowchart", "data": parsed}

    elif command == "activities":

        activity = generate_activity(topic)

        return {"type": "activity", "data": activity}

    else:

        notes = generate_notes(topic, time_data["target_words"])

        return {
            "type": "notes",
            "data": notes,
            "structure": time_data
        }