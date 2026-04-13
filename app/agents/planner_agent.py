from app.agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("PlannerAgent")

    def run(self, input_data: dict) -> dict:
        query = input_data.get("query")

        # Dummy breakdown (we improve later using LLM)
        tasks = [
            "generate_sql",
            "analyze_data",
            "generate_insight"
        ]

        return {
            "tasks": tasks,
            "original_query": query
        }