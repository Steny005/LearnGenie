from datetime import datetime


def build_lesson_state(
    topic: str,
    module: str,
    duration_minutes: int,
    notes_text: str,
    activity_data: dict
):

    # Extract first sentence from notes
    first_sentence = notes_text.split(".")[0].strip() + "."

    # Current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    return {
        "date": current_date,
        "duration_minutes": duration_minutes,
        "module": module,
        "topic_name": topic,
        "note_in_one_sentence": first_sentence,
        "activity_heading": activity_data.get("title")
    }