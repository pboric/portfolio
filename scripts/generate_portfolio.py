import sys
import requests

HEADER = """
# Petar Krešimir Borić

[![Email](https://img.shields.io/badge/email-kresimirepet@gmail.com-blue?style=flat-square&logo=gmail)](mailto:kresimirepet@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-petarkboric-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/petarkboric)
[![GitHub](https://img.shields.io/badge/GitHub-petarkresimirboric-black?style=flat-square&logo=github)](https://github.com/petarkresimirboric)

*Data Scientist · AI Developer · Environmental Engineer*

---

## Professional Summary

Versatile Data Scientist with a background in environmental engineering and experience delivering machine learning and NLP solutions. Skilled in Python, BERT, RAG, and AI fairness. Strong in building end-to-end pipelines for real-world datasets.

---

## Technical Skills

- **Programming:** Python, Jupyter, SQL, Git, PySpark, Databricks  
- **ML & DL:** Classification (multi-label, multi-class), Transformers (BERT), multi-task learning, fairness mitigation  
- **NLP:** Text classification, Q&A with RAG, fake/toxic comment detection  
- **Tools:** scikit-learn, pandas, NumPy, matplotlib, PyTorch, TensorFlow, Hugging Face  
- **Data Science:** EDA, feature engineering, PCA, credit/risk prediction  
- **BI & Viz:** Power BI, Looker, Dash  
- **Soft Skills:** Analytical thinking, teamwork, documentation

---

## Experience

**2023–2024 – WWTP Manager, Riko d.o.o., Zagreb, Croatia**  
• Developed Python tools for wastewater optimization and metrics tracking  
• Led predictive modeling and promoted digital workflows  

**2023 – Sensor Applications Intern, OxyIe, Zurich, Switzerland**  
• Analyzed sensory data for water quality using ML  
• Automated scraping/API pipelines for data ingestion  

**2018–2021 – Teaching Assistant, University of Zagreb, Zagreb, Croatia**  
• Instructed Python for statistics and scientific computing  

---

## Education

- **2023–2025:** Data Science & AI, Turing College, Remote  
- **2020–2022:** MSc in Environmental Engineering, University of Zagreb, Zagreb, Croatia  
- **2021–2022:** Erasmus Exchange Program, University of Chemistry and Technology, Prague, CZ

---

## Certifications & Projects

**Certifications:**  
- Python (HackerRank), SQL Intermediate (HackerRank), Data Analysis (freeCodeCamp)

**Highlighted Projects:**  
- **Credit Risk:** LightGBM + PySpark pipeline  
- **NLP:** BERT models for fake/toxic content  
- **RAG Q&A:** Transformer-based retrieval + generation  
- **Web Scraping:** Selenium/API automation  

---

## Languages

- **English:** Professional Proficiency  
- **Croatian:** Native  
- **German:** Basic  

---
"""

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
    lines.append(HEADER)
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
