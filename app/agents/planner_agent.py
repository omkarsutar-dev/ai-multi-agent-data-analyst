from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a data analyst AI."),
    ("human", """
Break the query into steps.

If the query refers to previous results (like "why", "this", "that"):
- Use previous context instead of generating new SQL

Available tasks:
- generate_sql
- analyze_data
- generate_insight

Query:
{query}

Context:
{context}

Return ONLY a list.
""")
])

def planner_node(state):
    query = state["query"]
    history = state.get("history", [])

    context = ""
    if history:
        last = history[-1]
        context = f"Previous Query: {last['query']}\nPrevious Insight: {last['insight']}"

    response = llm.invoke(
        prompt.format_messages(query=query, context=context)
    )

    try:
        tasks = eval(response.content)
    except:
        tasks = ["generate_sql", "analyze_data"]

    return {
        "tasks": tasks,
        "retry_count": 0
    }