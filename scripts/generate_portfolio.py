import sys
import requests

HEADER = """
# Petar Krešimir Borić

[![Email](https://img.shields.io/badge/email-kresimirpet@gmail.com-blue?style=flat-square&logo=gmail)](mailto:kresimirpet@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-petarkboric-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/petarkboric)
[![GitHub](https://img.shields.io/badge/GitHub-pboric-black?style=flat-square&logo=github)](https://github.com/pboric)

*Data Scientist · AI Developer · Environmental Engineer*

---

## Professional Summary

Data scientist with a background in environmental engineering, now working on air-quality data analysis and instrument calibration at IMI in Zagreb. My current project corrects low-cost particulate-matter sensors against official reference stations during Saharan dust episodes, using LightGBM and Copernicus CAMS data. Experienced in end-to-end machine learning on real-world data, from exploratory analysis and statistics to tuned and deployed models, including NLP and computer vision with PyTorch and Hugging Face.

---

## Technical Skills

- **Programming:** Python, Jupyter, SQL, Git, PySpark, Databricks  
- **ML & DL:** Gradient boosting (LightGBM, XGBoost), hyperparameter tuning (Optuna), classification (multi-label, multi-class), Transformers (BERT, DistilBERT), multi-task learning, fairness mitigation  
- **Environmental data:** Air-quality monitoring data (EEA), low-cost sensors, ERA5 weather and Copernicus CAMS data, sensor calibration  
- **Statistics:** Hypothesis testing, confidence intervals, bootstrap, leakage-free cross-validation  
- **NLP:** Text classification, Q&A with RAG, toxic comment detection  
- **Data collection:** Web scraping and API pipelines (Selenium, requests)  
- **Tools:** scikit-learn, pandas, NumPy, matplotlib, PyTorch, TensorFlow, Hugging Face  
- **Data Science:** EDA, feature engineering, PCA, credit/risk prediction  
- **BI & Viz:** Power BI, Looker, Dash  
- **Soft Skills:** Analytical thinking, teamwork, documentation

---

## Experience

**2026–present – Research Assistant, Institute for Medical Research and Occupational Health (IMI), Zagreb, Croatia**
• Air-quality data analysis and instrument calibration, Environmental Hygiene Unit

**2023–2024 – WWTP Manager, Riko d.o.o., Zagreb, Croatia**  
• Developed Python tools for wastewater optimization and metrics tracking  
• Led predictive modeling and promoted digital workflows  

**2023 – Sensor Applications Intern, Oxyle, Zurich, Switzerland**  
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

## Certifications

- Python (HackerRank), SQL Intermediate (HackerRank), Data Analysis (freeCodeCamp)

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
        params = {'per_page': 100, 'page': page, 'sort': 'created'}  # newest first
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Failed to fetch repos:", response.text)
            sys.exit(1)
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    # Filter out forks, this portfolio repo and the profile README repo; sort by stars (descending)
    skip = {"portfolio", username.lower()}
    repos = [r for r in repos if not r.get("fork") and r["name"].lower() not in skip]
    repos.sort(key=lambda r: r["stargazers_count"], reverse=True)
    return repos

# Featured projects, in this order, with a short summary and the main result.
# Everything else is listed below them from the GitHub repo descriptions.
FEATURED = [
    ("pm-sensor-correction",
     "Corrects low-cost PM sensors against official EEA reference stations during Saharan dust, smoke and humid air, "
     "using weather data and Copernicus CAMS forecasts. Tested on areas the model never saw, a LightGBM model cuts the "
     "PM10 error in dust episodes by 40% compared with the standard humidity correction."),
    ("credit-risk-prediction",
     "Credit default model on the Home Credit data: features from several linked tables, LightGBM and XGBoost tuned "
     "with Optuna, stacking and threshold tuning (ROC AUC 0.79), deployed as a FastAPI service."),
    ("age-gender-prediction",
     "Multi-task deep learning model that predicts age and gender from face images, improved over three versions, "
     "with bias analysis across age groups and gender (age error 4.3 years, gender accuracy 91%)."),
    ("toxic-comment-classification",
     "Multi-label toxic comment detection with DistilBERT, class weighting and tuned decision thresholds "
     "(ROC AUC 0.99 per class)."),
    ("spaceship-titanic-classification",
     "Tabular classification end to end: statistical tests, feature engineering and a stacking ensemble "
     "(ROC AUC 0.89, accuracy 80%)."),
]


def anchor(name):
    return name.lower().replace(' ', '-')


def make_portfolio_md(username, repos):
    by_name = {r["name"]: r for r in repos}
    featured = [(by_name[n], text) for n, text in FEATURED if n in by_name]
    featured_names = {r["name"] for r, _ in featured}
    others = [r for r in repos if r["name"] not in featured_names]

    lines = []
    lines.append(HEADER)
    lines.append("## Featured Projects\n")
    for repo, text in featured:
        lines.append(f"### <a name=\"{anchor(repo['name'])}\"></a>[{repo['name']}]({repo['html_url']})")
        lines.append(f"{text}  ")
        topics = repo.get("topics") or []
        if topics:
            lines.append("**Topics:** " + " · ".join(f"`{t}`" for t in topics))
        lines.append("")
    lines.append("---\n")
    lines.append("## Other Projects\n")

    # Table of Contents
    lines.append("### Table of Contents")
    for repo in others:
        name = repo["name"]
        lines.append(f"- [{name}](#{anchor(name)})")
    lines.append("\n---\n")

    # Project Details
    for repo in others:
        name = repo["name"]
        desc = repo["description"] or "_No description provided._"
        url = repo["html_url"]
        homepage = repo.get("homepage")
        language = repo.get("language") or "Unknown"

        # Trailing double spaces keep each field on its own line in Markdown
        lines.append(f"### <a name=\"{name.lower().replace(' ', '-')}\"></a>[{name}]({url})")
        lines.append(f"**Language:** {language}  ")
        lines.append(f"{desc}  ")
        if homepage:
            lines.append(f"**[Live Demo]({homepage})**")
        topics = repo.get("topics") or []
        if topics:
            lines.append("**Topics:** " + " · ".join(f"`{t}`" for t in topics))
        lines.append('\n---\n')
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
