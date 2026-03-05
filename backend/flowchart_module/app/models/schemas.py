from pydantic import BaseModel
from typing import List


class FlowchartRequest(BaseModel):
    input_text: str


class Node(BaseModel):
    id: str
    text: str


class Edge(BaseModel):
    from_node: str
    to_node: str


class FlowchartResponse(BaseModel):
    nodes: List[Node]
    edges: List[Edge]