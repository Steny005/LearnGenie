def format_activity(activity_data: dict):

    return {
        "activity_title": activity_data.get("title"),
        "objective": activity_data.get("objective"),
        "procedure": activity_data.get("procedure"),
        "expected_outcome": activity_data.get("expected_outcome"),
        "engagement_type": "Gen-Z Interactive",
        "memory_focus": True
    }