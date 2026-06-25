from typing import TypedDict

class AgentState(TypedDict, total=False):
    issue_url: str

    owner: str
    repo: str
    issue_number: int
    issue_title: str
    issue_body: str

    implementation_plan: str
    error: str
    