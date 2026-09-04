github_repo_tool = {
    "type": "function",
    "function": {
        "name": "get_github_repo_stats",
        "description": (
            "Get current statistics and metadata "
            "for a GitHub repository."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "repo_url": {
                    "type": "string",
                    "description": "Full GitHub repository URL.",
                }
            },
            "required": ["repo_url"],
            "additionalProperties": False,
        },
    },
}