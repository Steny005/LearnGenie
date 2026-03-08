def calculate_target_words(duration_minutes):

    intro = duration_minutes * 0.10
    explanation = duration_minutes * 0.50
    examples = duration_minutes * 0.20

    note_minutes = explanation + examples

    activities = duration_minutes * 0.15
    recap = duration_minutes * 0.05

    # MVP compression factor
    target_words = int(note_minutes * 14)

    return {
        "intro": round(intro),
        "explanation": round(explanation),
        "examples": round(examples),
        "activities": round(activities),
        "recap": round(recap),
        "target_words": target_words
    }