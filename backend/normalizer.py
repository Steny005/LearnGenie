from pydantic import BaseModel
class CoreInput(BaseModel):
    topic: str
    content: str
    class_level: str
    duration_minutes: int
    teaching_mode: str
    complexity: str
    include_flowchart: bool = True
    include_activities: bool = True
    include_lesson_plan: bool = True
