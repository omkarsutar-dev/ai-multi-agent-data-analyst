from app.core.memory_store import get_memory, add_memory

# 🔹 Retrieve memory
def memory_retrieve_node(state):
    history = get_memory()

    return {
        "history": history[-3:]   # last 3 interactions
    }


# 🔹 Store memory
def memory_store_node(state):
    query = state["query"]
    insight = state.get("insight", "")

    entry = {
        "query": query,
        "insight": insight
    }

    add_memory(entry)

    return {}