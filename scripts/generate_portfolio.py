import sys
import requests

def get_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos"
        params = {'per_page': 100, 'page': page, 'sort': 'updated'}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Failed to fetch repos:", response.text)
            sys.exit(1)
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def make_portfolio_md(username, repos):
    lines = []
    lines.append(f"# {username}'s Portfolio\n")
    lines.append(f"Generated automatically by [GitHub Actions](https://github.com/features/actions).\n")
    lines.append("## Projects\n")
    for repo in repos:
        if repo.get("fork"):
            continue  # Skip forks
        name = repo["name"]
        desc = repo["description"] or "No description."
        url = repo["html_url"]
        homepage = repo.get("homepage")
        lines.append(f"### [{name}]({url})")
        lines.append(f"{desc}")
        if homepage:
            lines.append(f"[Live Demo]({homepage})")
        lines.append(f"- ⭐ Stars: {repo['stargazers_count']} | 🍴 Forks: {repo['forks_count']}\n")
    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_portfolio.py <github-username>")
        sys.exit(1)
    username = sys.argv[1]
    repos = get_repos(username)
    md = make_portfolio_md(username, repos)
    with open("portfolio.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Portfolio generated as portfolio.md")