# Insurance Risk Analytics & Predictive Modeling

This repository contains an end-to-end data science pipeline built during **10 Academy's AI Mastery Week 3 Challenge**. The goal is to help **AlphaCare Insurance Solutions (ACIS)** improve risk segmentation, optimize premium pricing, and identify low-risk, high-value customers using historical South African car insurance data.

---

## 📌 Project Overview

This project addresses key business questions for ACIS by:

- Analyzing and visualizing customer and claim data
- Performing A/B testing to validate pricing strategies
- Building regression and classification models to predict:
  - Expected annual premium (`regression`)
  - Risk level of a customer (`classification`)
- Interpreting model outputs using SHAP
- Managing reproducibility with DVC

---

## 📊 Key Components

### 1. 📁 Data
- `train.csv`, `test.csv` – anonymized customer and claim-level data
- Structured into:
  - Demographic information
  - Driving behavior
  - Claims and premium details

### 2. 🔍 Exploratory Data Analysis (EDA)
- Univariate & bivariate analysis
- Risk segmentation by age, claim history, gender, and region
- Premium vs claim behavior visualization

### 3. 📈 Statistical Testing
- A/B testing to evaluate if new pricing strategies outperform existing ones
- Hypothesis testing on average premiums and risk levels

### 4. 🧠 Predictive Modeling
- **Regression Model:** Predict customer's annual premium
- **Classification Model:** Predict whether a customer is high- or low-risk
- Model Evaluation: RMSE, Accuracy, ROC-AUC

### 5. 🔁 DVC (Data Version Control)
- Tracks data, models, and outputs
- Ensures reproducibility

### 6. 🧠 Model Interpretation
- SHAP values to understand which features drive risk and premium predictions

---

## 🧪 Tech Stack

| Tool / Library         | Purpose                          |
|------------------------|----------------------------------|
| Python, pandas, NumPy  | Data manipulation                |
| Matplotlib, seaborn    | Visualization                    |
| Scikit-learn, XGBoost  | Modeling                         |
| SHAP                   | Model interpretability           |
| DVC                    | Experiment and data tracking     |
| Jupyter Notebook       | Interactive development          |

---

## 🏁 Getting Started

### ✅ Prerequisites
- Python 3.8+
- Git & DVC installed

### 📦 Installation
```bash
git clone https://github.com/Alki45/insurance-risk-analytics-predictive-modeling.git
cd insurance-risk-analytics-predictive-modeling
pip install -r requirements.txt
