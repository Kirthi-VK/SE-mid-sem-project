from agents.coordinator_agent import CoordinatorAgent


def main():

    print("\nMulti-Agent Research Assistant\n")

    query = input("Enter research topic: ")

    coordinator = CoordinatorAgent()

    result = coordinator.run(query)

    print("\n=== FINAL SUMMARY ===\n")

    print(result)


if __name__ == "__main__":
    main()