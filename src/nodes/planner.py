import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from src.state import AgentState, AgentStateUpdate

load_dotenv()

def planner_node(state: AgentState) -> AgentStateUpdate:
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    owner = state.get("owner")
    repo = state.get("repo")
    issue_number = state.get("issue_number")
    issue_title = state.get("issue_title")
    issue_body = state.get("issue_body") or "No issue body provided."

    if not owner or not repo or issue_number is None or not issue_title:
        raise ValueError("Planner node requires issue details from issue_reader node.")

    llm = ChatOpenAI(
        model=model_name,
        temperature=0
    )

    system_message = SystemMessage(
        content=(
            "You are a senior AI software engineer. "
            "Given a GitHub issue, create a practical implementation plan. "
            "Do not write code yet. Focus on what files may need inspection, "
            "what behavior likely needs changing, what tests should be run, "
            "and what risks to watch for."
        )
    )

    human_message = HumanMessage(
        content=(
            f"Repository: {owner}/{repo}\n"
            f"Issue #{issue_number}: {issue_title}\n\n"
            f"Issue body:\n{issue_body}"
        )
    )

    response = llm.invoke([system_message, human_message])
    implementation_plan = response.content

    if not isinstance(implementation_plan, str):
        implementation_plan = str(implementation_plan)

    return {
        "implementation_plan": implementation_plan
    }
