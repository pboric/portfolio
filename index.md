# Petar Krešimir Borić’s Portfolio

[![Email](mailto:kresimirepet@gmail.com)](mailto:kresimirepet@gmail.com) [![LinkedIn](https://www.linkedin.com/in/petarkboric)](https://www.linkedin.com/in/petarkboric) [![GitHub](https://github.com/petarkresimirboric)](https://github.com/petarkresimirboric)  
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

## Projects

### Table of Contents

{% for repo in repos %}
- [{{ repo.name }}](#{{ repo.name | lower | replace(" ", "-") }})
{% endfor %}

---

{% for repo in repos %}
### <a name="{{ repo.name | lower | replace(" ", "-") }}"></a>[{{ repo.name }}]({{ repo.html_url }})
**Language:** {{ repo.language or "Unknown" }}
{{ repo.description or "_No description provided._" }}
{% if repo.homepage %}
**[Live Demo]({{ repo.homepage }})**
{% endif %}
![Stars](https://img.shields.io/github/stars/{{ username }}/{{ repo.name }}?style=social) ![Forks](https://img.shields.io/github/forks/{{ username }}/{{ repo.name }}?style=social)

---
{% endfor %}
