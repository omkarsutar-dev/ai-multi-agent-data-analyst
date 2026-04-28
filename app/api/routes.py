from fastapi import APIRouter
from app.graph.graph_builder import build_graph
from app.api.schemas import AnalyzeResponse
from app.core.logger import logger
from app.api.schemas import AnalyzeRequest, AnalyzeResponse

router = APIRouter()
graph = build_graph()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    try:
        query = request.query
        query = query.strip('"')
        logger.info(f"Received query: {query}")

        result = graph.invoke({
            "query": query,
            "data": None,
            "history": [],
            "retry_count": 0
        })

        logger.info("Graph execution completed")

        # ✅ Clean response
        response = AnalyzeResponse(
            query=query,
            insight=result.get("insight", ""),
            data=result.get("data", None),
            chart_path=result.get("chart_path", ""),
            is_valid=result.get("is_valid", True),
            feedback=result.get("feedback", "")
        )

        return response

    except Exception as e:
        logger.error(f"Error: {str(e)}")

        return AnalyzeResponse(
            query=request.query,
            insight="Something went wrong. Please try again.",
            is_valid=False,
            feedback=str(e)
        )