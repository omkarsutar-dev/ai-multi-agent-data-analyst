from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm
import json

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
- If data is provided → analyze it
- If context is provided → use previous insight
- Max 3–4 bullet points
- Focus on key insights only
- Avoid repetition
- Avoid generic statements
- Include possible reasons if trends are visible
- Use ONLY provided data/context
- DO NOT assume external reasons (like marketing, demographics)
- If unsure → say "possible reasons cannot be determined from data"
- Be concise

Answer:
""")
])

def insight_node(state):
    query = state["query"]
    data = state.get("data", None)
    history = state.get("history", [])

    # 🔥 CASE 1: No data → use memory
    if not data:
        if history:
            last = history[-1]
            context = f"""
                Previous Query: {last['query']}
                Previous Insight: {last['insight']}
                """
        else:
            context = "No previous context available."

        response = llm.invoke(
            prompt.format_messages(
                query=query,
                data=context   # 👈 reuse same variable
            )
        )

        return {
            "insight": response.content.strip()
        }

    # 🔥 CASE 2: Normal data flow
    formatted_data = json.dumps(data, indent=2)

    response = llm.invoke(
        prompt.format_messages(query=query, data=formatted_data)
    )

    return {
        "insight": response.content.strip()
    }