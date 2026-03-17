from orchestral import Agent
from orchestral.llm import Ollama


def create_summary_agent():

    agent = Agent(
        llm=Ollama(model="tinyllama:latest"),
        system_prompt="""
        You summarize research papers.

        Provide:
        - Key idea
        - Method
        - Contribution
        - Limitations
        """
    )

    return agent