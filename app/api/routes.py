from fastapi import APIRouter
from app.services.orchestrator import Orchestrator

router = APIRouter()
orchestrator = Orchestrator()

@router.post("/analyze")
def analyze(query: str):
    result = orchestrator.run(query)
    return result