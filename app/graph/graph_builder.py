from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.agents.planner_agent import planner_node
from app.agents.sql_agent import sql_node, execute_sql_node

def build_graph():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("planner", planner_node)
    graph.add_node("sql_generator", sql_node)
    graph.add_node("sql_executor", execute_sql_node)

    # Flow
    graph.set_entry_point("planner")
    graph.add_edge("planner", "sql_generator")
    graph.add_edge("sql_generator", "sql_executor")
    graph.add_edge("sql_executor", END)

    return graph.compile()