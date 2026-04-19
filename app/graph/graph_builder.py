from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.agents.planner_agent import planner_node

def build_graph():
    graph = StateGraph(AgentState)

    # Add nodes
    graph.add_node("planner", planner_node)

    # Define flow
    graph.set_entry_point("planner")
    graph.add_edge("planner", END)

    return graph.compile()