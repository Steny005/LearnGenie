import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import UploadFile, File

from pdf_parser import extract_text_from_pdf
from notes_generator import generate_notes
from activity_generator import generate_activity
from duration_logic import calculate_target_words

from summariser import summarize_long_text, clean_text

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
    """
    Detects commands like:
    @flowchart
    @activities
    """

    text_lower = text.lower().strip()

    if any(cmd in text_lower for cmd in ["@flowchart", "@chart", "@flow"]):
        topic = re.sub(r"@(flowchart|chart|flow)[a-z]*", "", text, flags=re.IGNORECASE).strip()
        return topic, "flowchart"

    if any(cmd in text_lower for cmd in ["@activity", "@activities", "@act"]):
        topic = re.sub(r"@(activities|activity|act)[a-z]*", "", text, flags=re.IGNORECASE).strip()
        return topic, "activities"

    if text_lower.endswith("flowchart") or text_lower.endswith("flow chart"):
        topic = re.sub(r"(flowchart|flow chart)$", "", text, flags=re.IGNORECASE).strip()
        return topic, "flowchart"

    if text_lower.endswith("activity") or text_lower.endswith("activities"):
        topic = re.sub(r"(activity|activities)$", "", text, flags=re.IGNORECASE).strip()
        return topic, "activities"

    return text.strip(), "notes"


@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):

    text = extract_text_from_pdf(file.file)

    # clean extracted text
    text = clean_text(text)

    # summarize if long
    if len(text.split()) > 10:
        topic = summarize_long_text(text)
    else:
        topic = text

    # safety cap
    topic = topic[:200]

    return {
        "topic_text": topic
    }


@app.post("/generate")
def generate(data: UserInput):

    try:

        topic, command = detect_command(data.text)

        # clean pasted text / transcript
        topic = clean_text(topic)

        # summarize long input
        if len(topic.split()) > 10:
            topic = summarize_long_text(topic)

        # safety cap so generator stays fast
        topic = topic[:200]

        if not topic:
            raise HTTPException(status_code=400, detail="Topic cannot be empty")

        time_data = calculate_target_words(data.duration)

        if command == "flowchart":

            raw = generate_flowchart_from_llm(topic)
            parsed = extract_valid_json(raw)

            return {
                "type": "flowchart",
                "data": parsed
            }

        elif command == "activities":

            activity = generate_activity(topic)

            return {
                "type": "activity",
                "data": activity
            }

        else:

            notes = generate_notes(topic, time_data)

            return {
                "type": "notes",
                "data": notes,
                "structure": time_data
            }

    except Exception as e:

        print(f"Error generating: {str(e)}")

        if isinstance(e, HTTPException):
            raise e

        raise HTTPException(
            status_code=500,
            detail=f"Generation failed: {str(e)}"
        )