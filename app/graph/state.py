from typing import TypedDict, List

class AgentState(TypedDict):
    query: str
    tasks: List[str]