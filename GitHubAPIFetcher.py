import requests
from typing import List

class GitHubAPI:
    def __init__(self, username: str):
        self.username = username

    def get_repositories(self) -> List[str]:
        try:
            url = f"https://api.github.com/users/{self.username}/repos"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
            repositories = [repo["name"] for repo in response.json()]
            return repositories
        except requests.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []

# Example Usage:
if __name__ == "__main__":
    username = "piyushbhavsarr"
    github_api = GitHubAPI(username)

    try:
        repositories = github_api.get_repositories()
        if repositories:
            print(f"Repositories for {username}:")
            for index, repo in enumerate(repositories, start=1):
                print(f"{index}. {repo}")
        else:
            print("No repositories found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")