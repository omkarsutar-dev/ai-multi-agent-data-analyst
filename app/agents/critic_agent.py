from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm
import json
import re


llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict data analyst reviewer."),
    ("human", """
Validate the insight using the data.

Query:
{query}

Data:
{data}

Insight:
{insight}

Rules:
- Respond ONLY in valid JSON
- Do NOT include explanation outside JSON
- No markdown, no extra text

Format:
{{"is_valid": true, "feedback": "reason"}}
""")
])


def extract_json(text: str):
    # Extract JSON block using regex
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group(0)
    return "{}"


def critic_node(state):
    query = state["query"]
    data = state["data"]
    insight = state["insight"]

    formatted_data = json.dumps(data, indent=2)

    response = llm.invoke(
        prompt.format_messages(
            query=query,
            data=formatted_data,
            insight=insight
        )
    )

    raw_output = response.content

    try:
        clean_json = extract_json(raw_output)
        result = json.loads(clean_json)
    except Exception as e:
        result = {
            "is_valid": result.get("is_valid", True),
            "feedback": result.get("feedback", "No feedback")
        }

    return result