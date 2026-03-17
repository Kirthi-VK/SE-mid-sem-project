from agents.search_agent import create_search_agent
from agents.summary_agent import create_summary_agent


class CoordinatorAgent:

    def __init__(self):
        self.search_agent = create_search_agent()
        self.summary_agent = create_summary_agent()

    def run(self, query):

        print("\n--- Searching Papers ---\n")

        papers = self.search_agent.run(query)

        print(papers)

        print("\n--- Summarizing Papers ---\n")

        # Convert message to text
        papers_text = str(papers)

        summary = self.summary_agent.run(
            f"Summarize the following research papers in 3 bullet points:\n{papers_text[:500]}"
        )

        return summary