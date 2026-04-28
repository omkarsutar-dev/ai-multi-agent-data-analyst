from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.agents.planner_agent import planner_node
from app.agents.sql_agent import sql_node, execute_sql_node
from app.agents.insight_agent import insight_node
from app.agents.critic_agent import critic_node
from app.agents.memory_agent import memory_retrieve_node, memory_store_node

def build_graph():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("memory_retrieve", memory_retrieve_node)
    graph.add_node("planner", planner_node)
    graph.add_node("sql_generator", sql_node)
    graph.add_node("sql_executor", execute_sql_node)
    graph.add_node("insight_generator", insight_node)
    graph.add_node("critic", critic_node)
    graph.add_node("memory_store", memory_store_node)

    # Flow
    graph.set_entry_point("memory_retrieve")
    graph.add_edge("memory_retrieve", "planner")
    graph.add_edge("planner", "sql_generator")
    graph.add_edge("sql_generator", "sql_executor")
    graph.add_edge("sql_executor", "insight_generator")
    graph.add_edge("insight_generator", "critic")

    # Conditional logic
    def should_retry(state):
        is_valid = state.get("is_valid", True)
        retry_count = state.get("retry_count", 0)

        # STOP CONDITION
        if retry_count > 2:
            return "end"

        # 🔁 Retry if invalid
        if not is_valid:
            return "retry"

        return "end"

    graph.add_conditional_edges(
        "critic",
        should_retry,
        {
            "retry": "insight_generator",
            "end": "memory_store"
        }
    )

    graph.add_edge("memory_store", END)

    return graph.compile()