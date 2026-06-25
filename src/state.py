from typing import NotRequired, TypedDict

class AgentState(TypedDict):
    issue_url: str

    owner: NotRequired[str]
    repo: NotRequired[str]
    issue_number: NotRequired[int]
    issue_title: NotRequired[str]
    issue_body: NotRequired[str]

    implementation_plan: NotRequired[str]
    error: NotRequired[str]


class AgentStateUpdate(TypedDict, total=False):
    issue_url: str

    owner: str
    repo: str
    issue_number: int
    issue_title: str
    issue_body: str

    implementation_plan: str
    error: str
