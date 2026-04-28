from typing import TypedDict, List, Any

class AgentState(TypedDict):
    query: str
    tasks: List[str]
    sql_query: str
    data: Any
    insight: str