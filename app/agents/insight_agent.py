from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior data analyst."),
    ("human", """
Analyze the data and answer the query.

Query:
{query}

Data:
{data}

Rules:
- Max 3–4 bullet points
- Focus on key insights only
- Avoid repetition
- No generic statements
- Include possible reasons if trends are visible

Answer:
""")
])

def insight_node(state):
    query = state["query"]
    data = state["data"]

    response = llm.invoke(
        prompt.format_messages(query=query, data=str(data))
    )

    return {
        "insight": response.content.strip()
    }