from fastapi import APIRouter, HTTPException

from app.models.schemas import FlowchartRequest
from app.services.llm_service import generate_flowchart_from_llm
from app.utils.parser import extract_valid_json, enforce_sequential_edges

router = APIRouter()


@router.post("/generate")
async def generate_flowchart(request: FlowchartRequest):

    try:

        raw_output = generate_flowchart_from_llm(request.input_text)

        parsed = extract_valid_json(raw_output)
        parsed = enforce_sequential_edges(parsed)
        return parsed

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))