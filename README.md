# Fake News Data Processing & Classification Pipeline

## Project Overview

This project demonstrates an end-to-end Data Engineering and Machine Learning pipeline for Fake News Detection.

The pipeline extracts raw news data, performs validation and transformation, loads cleaned data into MySQL, conducts exploratory data analysis (EDA), engineers features using TF-IDF, and trains machine learning models to classify news as Fake or Real.

---

## Objectives

- Build a complete ETL pipeline
- Perform data quality validation
- Store processed data in MySQL
- Conduct exploratory data analysis
- Train and evaluate machine learning models
- Deploy a prediction pipeline

---

## Dataset

Source:
Fake and Real News Dataset

Files:

- Fake.csv
- True.csv

Total Records:

- Original Records: 44,898
- Clean Records: 44,058

---

## Project Architecture

Raw Data
↓
Extract
↓
Validate
↓
Transform
↓
Load (MySQL)
↓
EDA
↓
Feature Engineering
↓
Model Training
↓
Prediction

---

## Technologies Used

### Programming

- Python
- SQL

### Data Engineering

- ETL Pipeline
- Data Validation
- Data Cleaning
- Data Transformation

### Database

- MySQL

### Data Analysis

- Pandas
- NumPy
- Matplotlib

### Machine Learning

- Scikit-Learn
- TF-IDF
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### Version Control

- Git
- GitHub

---

## Folder Structure

fake_news_pipeline/

├── data/

│ ├── raw/

│ └── processed/

├── logs/

│ └── pipeline.log

├── models/

├── notebooks/

│ └── exploratory_analysis.ipynb

├── reports/

├── scripts/

├── sql/

├── README.md

├── requirements.txt

└── .gitignore

---

## ETL Pipeline

### Extract

- Loaded Fake.csv and True.csv
- Added labels
- Merged datasets

### Validate

- Checked missing values
- Identified duplicates
- Verified data quality

### Transform

- Removed duplicates
- Removed empty records
- Cleaned text data
- Standardized format

### Load

- Loaded processed data into MySQL

---

## Data Quality Report

| Metric | Count |
|----------|----------|
| Original Records | 44,898 |
| Duplicate Records | 209 |
| Empty Records | 631 |
| Clean Records | 44,058 |

---

## Exploratory Data Analysis

Performed:

- Fake vs Real News Analysis
- Subject Distribution Analysis
- News Length Analysis
- Missing Value Analysis

---

## Feature Engineering

Applied:

- TF-IDF Vectorization
- Train-Test Split

Training Data: 80%

Testing Data: 20%

---

## Machine Learning Models

Implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

---

## Prediction

The trained model predicts whether a news article is:

- Fake News
- Real News

---

## Results

- Successfully processed 44,898 news records
- Built a complete ETL pipeline
- Achieved high classification accuracy
- Integrated Data Engineering and Machine Learning workflows

---

