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
    # Filter out forks and sort by stars (descending)
    repos = [r for r in repos if not r.get("fork")]
    repos.sort(key=lambda r: r["stargazers_count"], reverse=True)
    return repos

def make_portfolio_md(username, repos):
    lines = []
    lines.append(f"# {username}’s Portfolio\n")
    lines.append(f"Generated automatically by [GitHub Actions](https://github.com/features/actions).\n")
    lines.append("## Projects\n")

    # Table of Contents
    lines.append("### Table of Contents")
    for repo in repos:
        name = repo["name"]
        lines.append(f"- [{name}](#{name.lower().replace(' ', '-')})")
    lines.append("\n---\n")

    # Project Details
    for repo in repos:
        name = repo["name"]
        desc = repo["description"] or "_No description provided._"
        url = repo["html_url"]
        homepage = repo.get("homepage")
        stars = repo["stargazers_count"]
        forks = repo["forks_count"]
        language = repo.get("language") or "Unknown"

        lines.append(f"### <a name=\"{name.lower().replace(' ', '-')}\"></a>[{name}]({url})")
        lines.append(f"**Language:** {language}")
        lines.append(f"{desc}")
        if homepage:
            lines.append(f"**[Live Demo]({homepage})**")
        # Live badges for stars and forks
        lines.append(f"![Stars](https://img.shields.io/github/stars/{username}/{name}?style=social) ![Forks](https://img.shields.io/github/forks/{username}/{name}?style=social)\n")
        lines.append('---\n')
    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_portfolio.py <github-username>")
        sys.exit(1)
    username = sys.argv[1]
    repos = get_repos(username)
    md = make_portfolio_md(username, repos)
    with open("index.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Portfolio generated as index.md")
