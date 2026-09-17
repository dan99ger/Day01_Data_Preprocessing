# 🧹 Day 01: Automated Data Preprocessing Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Pipeline-F7931E)
![License](https://img.shields.io/badge/License-MIT-green)

A modular, production-ready data preprocessing system built with Python, Pandas, and Scikit-Learn. This repository demonstrates how to handle missing data, perform feature scaling, encode categorical variables, and filter outliers without experiencing data leakage.

---

## 🛠️ Key Features

* **Outlier Handling:** Automated detection and replacement of non-realistic continuous values.
* **Leak-Free Pipelines:** Utilizes `ColumnTransformer` and `Pipeline` from Scikit-Learn to structure transformations safely.
* **Vectorized Processing:** Optimized data manipulation using pure Pandas and NumPy without explicit Python loops.
* **One-Hot Encoding:** Categorical feature mapping with dynamic column name recovery.

---

## 📂 Repository Structure

```text
Day01_Data_Preprocessing/
├── create_data.py          # Script to generate raw synthetic dataset with missing/outlier values
├── data_preprocessing.py    # Main production pipeline for data cleaning & scaling
├── raw_data.csv             # Raw input dataset
├── processed_data.csv       # Cleaned, scaled, and encoded output dataset
└── README.md                # Project documentation

```

---

## 🚀 How to Run

### 1. Setup Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pandas numpy scikit-learn

```

### 2. Generate Raw Dataset

```bash
python create_data.py

```

### 3. Execute Preprocessing Pipeline

```bash
python data_preprocessing.py

```

---

## 📊 Pipeline Overview

```text
Raw Data ➔ Outlier Replacement ➔ Missing Value Imputation ➔ Feature Scaling / One-Hot Encoding ➔ Processed Dataset

```

---
