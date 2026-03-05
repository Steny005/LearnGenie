def calculate_target_words(duration_minutes):

    intro = duration_minutes * 0.10
    explanation = duration_minutes * 0.50
    examples = duration_minutes * 0.20

    note_minutes = explanation + examples

    activities = duration_minutes * 0.15
    recap = duration_minutes * 0.05

    target_words = min(int(note_minutes * 25), 800) #less words more hardship for generation

    return {
        "intro": round(intro),
        "explanation": round(explanation),
        "examples": round(examples),
        "activities": round(activities),
        "recap": round(recap),
        "target_words": target_words
    }