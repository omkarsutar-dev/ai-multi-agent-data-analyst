from pydantic import BaseModel
from typing import Any, List


class AnalyzeRequest(BaseModel):
    query: str

class AnalyzeResponse(BaseModel):
    query: str
    insight: str
    data: Any = None
    chart_path: str = ""
    is_valid: bool = True
    feedback: str = ""

