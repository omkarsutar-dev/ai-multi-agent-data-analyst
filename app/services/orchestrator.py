from app.agents.planner_agent import PlannerAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()

    def run(self, query: str):
        # Step 1: Planning
        plan = self.planner.run({"query": query})

        return {
            "plan": plan
        }