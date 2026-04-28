from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a data analyst AI."),
    ("human", """
Break the user query into steps.

You MUST choose ONLY from these tasks:
- generate_sql
- analyze_data
- generate_insight

Return ONLY a Python list.

Query: {query}

Example Output:
["generate_sql", "analyze_data", "generate_insight"]
""")
])

def planner_node(state):
    query = state["query"]

    response = llm.invoke(
        prompt.format_messages(query=query)
    )

    try:
        tasks = eval(response.content)
    except:
        tasks = ["generate_sql", "analyze_data"]

    return {
        "tasks": tasks,
        "retry_count": 0
    }