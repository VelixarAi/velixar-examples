# CrewAI + Velixar — multi-agent system with shared memory
import os
from velixar import Velixar
from crewai import Agent, Task, Crew

v = Velixar(api_key=os.environ["VELIXAR_API_KEY"])


def store_memory(content: str, tags: list[str] = []) -> str:
    result = v.store(content, tags=tags)
    return f"Stored: {result.id}"


def recall_memory(query: str) -> str:
    results = v.search(query, limit=3)
    return "\n".join(f"- {m.content}" for m in results) or "No memories found."


researcher = Agent(
    role="Research Analyst",
    goal="Research topics and store findings in shared memory",
    backstory="You research topics thoroughly and save key findings for the team.",
    tools=[store_memory, recall_memory],
)

writer = Agent(
    role="Content Writer",
    goal="Recall research from memory and write summaries",
    backstory="You pull context from shared memory and write clear summaries.",
    tools=[recall_memory],
)

research_task = Task(
    description="Research the benefits of persistent AI memory. Store 3 key findings.",
    agent=researcher,
    expected_output="3 findings stored in memory",
)

write_task = Task(
    description="Recall the research findings from memory and write a brief summary.",
    agent=writer,
    expected_output="A 3-paragraph summary based on recalled findings",
)

crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task], verbose=True)

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)
