import requests


def get_github_repo_stats(repo_url: str):
    """
    Get current statistics for a GitHub repository.
    """

    # Extract owner/repo from:
    # https://github.com/huggingface/transformers
    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 2:
        return {"error": "Invalid GitHub repository URL"}

    owner = parts[-2]
    repo = parts[-1]

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return {
            "error": f"GitHub API returned status {response.status_code}"
        }

    data = response.json()

    return {
        "name": data["full_name"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "language": data["language"],
        "license": (
            data["license"]["spdx_id"]
            if data["license"]
            else None
        ),
    }