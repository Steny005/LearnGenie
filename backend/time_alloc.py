def calculate_time_distribution(duration_minutes: int):
    intro = duration_minutes * 0.10
    explanation = duration_minutes * 0.50
    examples = duration_minutes * 0.10
    activities = duration_minutes * 0.20
    recap = duration_minutes * 0.05
    
    note_minutes = explanation + examples
    target_words = int(note_minutes * 65) 

    return {
        "intro": round(intro),
        "explanation": round(explanation),
        "examples": round(examples),
        "activities": round(activities),
        "recap": round(recap),
        "target_words": target_words 
    }