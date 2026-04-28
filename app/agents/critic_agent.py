from langchain_core.prompts import ChatPromptTemplate
from app.core.llm import get_llm
import json
import re


llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict data analyst reviewer."),
    ("human", """
Validate the insight.

Query:
{query}

Context/Data:
{data}

Insight:
{insight}

Rules:
- If data is present → validate against data
- If context is present → validate against previous insight
- Return ONLY JSON

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
    insight = state["insight"]

    # 🔥 SAFE ACCESS
    data = state.get("data", None)
    history = state.get("history", [])

    # 🔥 CASE 1: No data → validate using memory
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
                data=context,
                insight=insight
            )
        )

    else:
        # 🔥 CASE 2: Normal validation
        import json
        formatted_data = json.dumps(data, indent=2)

        response = llm.invoke(
            prompt.format_messages(
                query=query,
                data=formatted_data,
                insight=insight
            )
        )

    # 🔥 SAFE JSON PARSING
    raw_output = response.content

    try:
        match = re.search(r'\{.*\}', raw_output, re.DOTALL)
        clean_json = match.group(0) if match else "{}"
        result = json.loads(clean_json)
    except:
        result = {
            "is_valid": True,
            "feedback": "Fallback: unable to validate"
        }

    # 🔥 NEW LOGIC
    retry_count = state.get("retry_count", 0)

    is_valid = result.get("is_valid", True)
    feedback = result.get("feedback", "")

    if not is_valid:
        retry_count += 1

    print(f"[CRITIC] is_valid={is_valid}, retry_count={retry_count}")  # debug

    return {
        "is_valid": is_valid,
        "feedback": feedback,
        "retry_count": retry_count
    }