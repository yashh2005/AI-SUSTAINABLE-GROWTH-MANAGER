from google_adk import Agent
from src.agents.planner import PlannerAgent
from src.agents.research import ResearchAgent
from src.agents.strategy import StrategyAgent
from src.agents.sustainability import SustainabilityAgent
from src.agents.reviewer import ReviewerAgent

# Create the ADK agent
agent = Agent(name="SustainableGrowthPlanner")

# Register your tools (each agent’s main function)
@agent.tool
def planner_tool(profile: dict) -> dict:
    return PlannerAgent().run(profile)

@agent.tool
def research_tool(profile: dict) -> dict:
    return ResearchAgent().run(profile)

@agent.tool
def strategy_tool(profile: dict) -> dict:
    return StrategyAgent().run(profile)

@agent.tool
def sustainability_tool(profile: dict) -> dict:
    return SustainabilityAgent().run(profile)

@agent.tool
def reviewer_tool(profile: dict) -> dict:
    return ReviewerAgent().run(profile)

# Run the agent interactively
if __name__ == "__main__":
    agent.run()