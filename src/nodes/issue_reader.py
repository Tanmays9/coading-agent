from src.github_client import fetch_github_issues
from src.state import AgentState, AgentStateUpdate

def issue_reader_node(state: AgentState) -> AgentStateUpdate:
    issue_url = state["issue_url"]

    issue = fetch_github_issues(issue_url)

    return {
        "owner": issue.owner,
        "repo": issue.repo,
        "issue_number": issue.issue_number,
        "issue_title": issue.title,
        "issue_body": issue.body
    }
