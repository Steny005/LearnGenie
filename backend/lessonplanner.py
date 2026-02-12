def generate_lesson_plan(duration, time_data):
    return {
        "total_duration": duration,
        "structure": [
            {"phase": "Introduction", "duration": time_data["intro"]},
            {"phase": "Explanation", "duration": time_data["explanation"]},
            {"phase": "Examples", "duration": time_data["examples"]},
            {"phase": "Activities", "duration": time_data["activities"]},
            {"phase": "Recap", "duration": time_data["recap"]}
        ]
    }
