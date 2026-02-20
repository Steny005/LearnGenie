from typing import Optional

def calculate_time_distribution(duration_minutes: Optional[int]):
    DEFAULT_DURATION = 45

    # Handle None or 0 safely
    if not duration_minutes or duration_minutes <= 0:
        duration_minutes = DEFAULT_DURATION

    # Time breakdown (can adjust later if needed)
    intro = duration_minutes * 0.10
    explanation = duration_minutes * 0.50
    examples = duration_minutes * 0.10
    activities = duration_minutes * 0.20
    recap = duration_minutes * 0.10  # balanced to complete 100%

    # Notes are mostly explanation + examples
    note_minutes = explanation + examples

    # Approximate words per teaching minute
    target_words = int(note_minutes * 65)

    return {
        "total_duration": duration_minutes,
        "intro": round(intro),
        "explanation": round(explanation),
        "examples": round(examples),
        "activities": round(activities),
        "recap": round(recap),
        "target_words": target_words
    }