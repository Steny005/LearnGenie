from pydantic import BaseModel
from typing import List, Optional
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
class NoteResponse(BaseModel):
    title: str
    estimated_word_count: int
    content: str

class FlowchartResponse(BaseModel):
    title: str
    structure: List[str]

class ActivityResponse(BaseModel):
    type: str
    title: str
    duration_minutes: int

class LessonPhase(BaseModel):
    phase: str
    duration: int

class LessonPlanResponse(BaseModel):
    total_duration: int
    structure: List[LessonPhase]

class GenerateResponse(BaseModel):
    notes: NoteResponse
    flowchart: Optional[FlowchartResponse]
    activities: Optional[List[ActivityResponse]]
    lesson_plan: Optional[LessonPlanResponse]


