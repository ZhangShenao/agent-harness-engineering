import sys
import os

# Ensure the project root is on sys.path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from deepagents import create_deep_agent

from quickstart.deep_research_agent.tools import internet_search
from quickstart.deep_research_agent.llm import llm

# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

# Create the agent
agent = create_deep_agent(
    model=llm,
    tools=[internet_search],
    system_prompt=research_instructions,
)

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "What is langgraph?"
    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(result["messages"][-1].content)
