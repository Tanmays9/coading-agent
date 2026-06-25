import os
import re
from dataclasses import dataclass

import requests
from dotenv import load_dotenv

load_dotenv()

@dataclass
class GitHubIssue:
    owner: str
    repo: str
    issue_number: int
    title: str
    body: str
    url: str


def parse_github_issue_url(issue_url: str) -> tuple[str, str, int]:
    pattern = r"https://github\.com/([^/]+)/([^/]+)/issues/(\d+)"
    match = re.match(pattern, issue_url.strip())

    if not match:
        raise ValueError(
            "Invalid Github issue URL. Expected format: "
            "https://github.com/owner/repo/issues/123"
        )
    
    owner, repo, issue_number = match.groups()
    return owner, repo, int(issue_number)


def fetch_github_issues(issue_url: str) -> GitHubIssue:
    owner, repo, issue_number = parse_github_issue_url(issue_url)

    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    headers = {
        "Accept": "application/vnd.github+json",
    }

    token = os.getenv("GITHUB_TOKEN")

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(api_url, headers=headers, timeout=20)

    if response.status_code == 404:
        raise RuntimeError("Issue not found. Check the URL or repository permissions.")

    if response.status_code == 403:
        raise RuntimeError("GitHub API rate limit or permission issue.")
    
    response.raise_for_status()

    data = response.json()

    return GitHubIssue(
        owner=owner,
        repo=repo,
        issue_number=issue_number,
        title=data.get("title", ""),
        body=data.get("body") or "",
        url=issue_url
    )
