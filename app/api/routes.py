from fastapi import APIRouter
from app.graph.graph_builder import build_graph

router = APIRouter()
graph = build_graph()

@router.post("/analyze")
def analyze(query: str):
    result = graph.invoke({
        "query": query
    })

    return result