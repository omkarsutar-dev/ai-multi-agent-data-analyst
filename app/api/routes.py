from fastapi import APIRouter
from app.graph.graph_builder import build_graph

router = APIRouter()
graph = build_graph()

@router.post("/analyze")
def analyze(query: str):
    query = query.strip('"')
    result = graph.invoke({
    "query": query,
    "data": None,
    "history": [],
    "retry_count": 0
    })

    return result