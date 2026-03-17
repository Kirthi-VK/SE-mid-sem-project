from orchestral import Agent
from orchestral.llm import Ollama


def create_search_agent():

    agent = Agent(
        llm=Ollama(model="phi3:mini"),
        system_prompt="""
        You are a research paper search assistant.

        When given a research topic:
        - Suggest 3 relevant academic paper titles
        - Briefly describe each paper

        Format:
        Paper 1:
        Paper 2:
        Paper 3:
        """
    )

    return agent