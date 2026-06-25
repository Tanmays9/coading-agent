import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from src.state import AgentState

load_dotenv()

def planner_node(state: AgentState) -> AgentState:
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

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
            f"Repository: {state['owner']}/{state['repo']}\n"
            f"Issue #{state['issue_number']}: {state['issue_title']}\n\n"
            f"Issue body:\n{state.get('issue_body') or 'No issue body provided.'}"
        )
    )

    response = llm.invoke([system_message, human_message])

    return {
        "implementation_plan": response.content
    }