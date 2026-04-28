from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI router."),
    ("human", """
Decide how to handle the query.

Options:
- sql → if data retrieval needed
- memory → if query refers to previous result
- insight → if general reasoning

Query:
{query}

History:
{history}

Rules:
- If query contains 'why', 'this', 'that' → memory
- If query asks for numbers/data → sql
- Else → insight

Return ONLY one word: sql / memory / insight
""")
])

def router_node(state):
    query = state["query"]
    history = state.get("history", [])

    response = llm.invoke(
        prompt.format_messages(query=query, history=str(history))
    )

    route = response.content.strip().lower()

    # safety fallback
    if route not in ["sql", "memory", "insight"]:
        route = "sql"

    return {
        "route": route
    }