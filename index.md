
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

## Featured Projects

### <a name="pm-sensor-correction"></a>[pm-sensor-correction](https://github.com/pboric/pm-sensor-correction)
Corrects low-cost PM sensors against official EEA reference stations during Saharan dust, smoke and humid air, using weather data and Copernicus CAMS forecasts. Tested on areas the model never saw, a LightGBM model cuts the PM10 error in dust episodes by 40% compared with the standard humidity correction.  
**Topics:** `air-quality` · `cams` · `copernicus` · `lightgbm` · `low-cost-sensors` · `particulate-matter` · `python` · `saharan-dust` · `sensor-calibration`

### <a name="credit-risk-prediction"></a>[credit-risk-prediction](https://github.com/pboric/credit-risk-prediction)
Credit default model on the Home Credit data: features from several linked tables, LightGBM and XGBoost tuned with Optuna, stacking and threshold tuning (ROC AUC 0.79), deployed as a FastAPI service.  
**Topics:** `credit-risk` · `fastapi` · `lightgbm` · `machine-learning` · `optuna` · `python` · `xgboost`

### <a name="age-gender-prediction"></a>[age-gender-prediction](https://github.com/pboric/age-gender-prediction)
Multi-task deep learning model that predicts age and gender from face images, improved over three versions, with bias analysis across age groups and gender (age error 4.3 years, gender accuracy 91%).  
**Topics:** `computer-vision` · `deep-learning` · `fairness` · `multi-task-learning` · `python` · `pytorch` · `utkface`

### <a name="toxic-comment-classification"></a>[toxic-comment-classification](https://github.com/pboric/toxic-comment-classification)
Multi-label toxic comment detection with DistilBERT, class weighting and tuned decision thresholds (ROC AUC 0.99 per class).  
**Topics:** `deep-learning` · `distilbert` · `multi-label-classification` · `nlp` · `python` · `pytorch` · `transformers`

### <a name="spaceship-titanic-classification"></a>[spaceship-titanic-classification](https://github.com/pboric/spaceship-titanic-classification)
Tabular classification end to end: statistical tests, feature engineering and a stacking ensemble (ROC AUC 0.89, accuracy 80%).  
**Topics:** `ensemble-learning` · `flask` · `kaggle` · `lightgbm` · `machine-learning` · `optuna` · `python` · `scikit-learn`

---

## Other Projects

### Table of Contents
- [concert-tour-rag-assistant](#concert-tour-rag-assistant)
- [Binary-Prediction-with-a-Rainfall-Dataset](#binary-prediction-with-a-rainfall-dataset)
- [Machine-Failure-Prediction](#machine-failure-prediction)
- [fake-news-detection](#fake-news-detection)
- [mushroom-classification](#mushroom-classification)
- [stroke-prediction](#stroke-prediction)
- [travel-insurance-prediction](#travel-insurance-prediction)
- [red-wine-quality-analysis](#red-wine-quality-analysis)
- [podcast-reviews-analysis](#podcast-reviews-analysis)
- [tech-mental-health-analysis](#tech-mental-health-analysis)
- [us-police-shootings-analysis](#us-police-shootings-analysis)
- [coursera-courses-analysis](#coursera-courses-analysis)
- [spotify-top-tracks-analysis](#spotify-top-tracks-analysis)
- [python-calculator-package](#python-calculator-package)

---

### <a name="concert-tour-rag-assistant"></a>[concert-tour-rag-assistant](https://github.com/pboric/concert-tour-rag-assistant)
**Language:** Python  
This repository contains a Python service that uses Retrieval Augmented Generation (RAG) to answer questions about concert tours in 2025-2026, based on ingested documents. It also includes an optional web search feature for artist concert information.  
**Topics:** `faiss` · `langchain` · `llama-cpp` · `llm` · `python` · `rag` · `sentence-transformers` · `streamlit`

---

### <a name="binary-prediction-with-a-rainfall-dataset"></a>[Binary-Prediction-with-a-Rainfall-Dataset](https://github.com/pboric/Binary-Prediction-with-a-Rainfall-Dataset)
**Language:** Jupyter Notebook  
A Kaggle challenge to train a model to predict rainfall for each day of the year.  
**Topics:** `classification` · `kaggle` · `lightgbm` · `machine-learning` · `python` · `weather` · `xgboost`

---

### <a name="machine-failure-prediction"></a>[Machine-Failure-Prediction](https://github.com/pboric/Machine-Failure-Prediction)
**Language:** Jupyter Notebook  
Project developed to predict machine failures using sensor data through dimensionality reduction (PCA) and machine learning. Achieved 87.3% accuracy with a tuned Random Forest model.  
**Topics:** `machine-learning` · `pca` · `predictive-maintenance` · `python` · `random-forest` · `scikit-learn`

---

### <a name="fake-news-detection"></a>[fake-news-detection](https://github.com/pboric/fake-news-detection)
**Language:** Jupyter Notebook  
A machine learning project that uses natural language processing and deep learning techniques to automatically classify news articles as real or fake. The project implements multiple models, from simple baselines to advanced BERT-based deep learning approaches.  
**Topics:** `bert` · `deep-learning` · `nlp` · `python` · `pytorch-lightning` · `text-classification` · `transformers`

---

### <a name="mushroom-classification"></a>[mushroom-classification](https://github.com/pboric/mushroom-classification)
**Language:** Jupyter Notebook  
This project focuses on building an improved machine learning model for mushroom classification.  
**Topics:** `deep-learning` · `image-classification` · `python` · `pytorch` · `pytorch-lightning` · `resnet`

---

### <a name="stroke-prediction"></a>[stroke-prediction](https://github.com/pboric/stroke-prediction)
**Language:** Jupyter Notebook  
Stroke risk prediction on an imbalanced dataset (1:19): EDA, chi-square tests and leakage-free resampling inside the training pipeline; logistic regression ROC AUC 0.84 on a held-out test set  
**Topics:** `classification` · `healthcare` · `machine-learning` · `python` · `scikit-learn` · `xgboost`

---

### <a name="travel-insurance-prediction"></a>[travel-insurance-prediction](https://github.com/pboric/travel-insurance-prediction)
**Language:** Jupyter Notebook  
This repository contains code and data related to predicting travel insurance purchases based on various features. The goal is to understand the factors influencing travel insurance decisions and build a predictive model.  
**Topics:** `classification` · `imbalanced-learn` · `machine-learning` · `python` · `scikit-learn` · `smote`

---

### <a name="red-wine-quality-analysis"></a>[red-wine-quality-analysis](https://github.com/pboric/red-wine-quality-analysis)
**Language:** Jupyter Notebook  
This project is dedicated to the analysis of red wine quality using various statistical and machine learning techniques. The analysis is performed using a Jupyter Notebook which provides an interactive environment to explore and visualize the data.  
**Topics:** `data-analysis` · `pandas` · `python` · `regression` · `statistics` · `statsmodels`

---

### <a name="podcast-reviews-analysis"></a>[podcast-reviews-analysis](https://github.com/pboric/podcast-reviews-analysis)
**Language:** Jupyter Notebook  
This repository provides an analysis of a Podcast Reviews Dataset.  
**Topics:** `data-analysis` · `hypothesis-testing` · `python` · `sentiment-analysis` · `sql` · `sqlite` · `statistics`

---

### <a name="tech-mental-health-analysis"></a>[tech-mental-health-analysis](https://github.com/pboric/tech-mental-health-analysis)
**Language:** Jupyter Notebook  
This repository contains an analysis of mental health issues within the tech industry. The analysis is conducted using survey data, exploring various aspects such as gender disparities, treatment-seeking behavior, and the correlation between corporate employment and mental health diagnoses.  
**Topics:** `data-analysis` · `eda` · `pandas` · `plotly` · `python` · `sql` · `sqlite`

---

### <a name="us-police-shootings-analysis"></a>[us-police-shootings-analysis](https://github.com/pboric/us-police-shootings-analysis)
**Language:** Jupyter Notebook  
Analysis & predictive modeling of the police shootings in USA  
**Topics:** `data-analysis` · `eda` · `jupyter-notebook` · `pandas` · `python` · `random-forest`

---

### <a name="coursera-courses-analysis"></a>[coursera-courses-analysis](https://github.com/pboric/coursera-courses-analysis)
**Language:** Jupyter Notebook  
This Jupyter notebook contains an exploratory data analysis of a dataset of Coursera courses. The goal of this analysis is to gain insights into the characteristics of the courses offered on the platform and understand the relationships between different variables.  
**Topics:** `data-visualization` · `eda` · `jupyter-notebook` · `pandas` · `python` · `seaborn`

---

### <a name="spotify-top-tracks-analysis"></a>[spotify-top-tracks-analysis](https://github.com/pboric/spotify-top-tracks-analysis)
**Language:** Jupyter Notebook  
Analysis of the top tracks on Spotify. Using pandas, numpy, and opendatasets libraries to download, manipulate, and analyze the data.  
**Topics:** `data-analysis` · `eda` · `jupyter-notebook` · `pandas` · `python` · `spotify`

---

### <a name="python-calculator-package"></a>[python-calculator-package](https://github.com/pboric/python-calculator-package)
**Language:** Python  
The Calculator package is a simple Python package that provides a Calculator class for performing basic arithmetic operations.  
**Topics:** `poetry` · `pytest` · `python` · `python-package`

---
