# Customer Churn Prediction - End-to-End Data Project

## Overview

This project predicts whether a telecom customer is likely to leave the service (Churn) using Machine Learning.

The project includes data extraction, cleaning, loading data into SQL Server, and building a classification model to predict customer churn.

---

## Project Workflow

CSV Dataset  
↓  
Data Cleaning & Transformation using Python  
↓  
Loading Data into SQL Server (ETL Pipeline)  
↓  
Machine Learning Model  
↓  
Customer Churn Prediction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SQL Server
- PyODBC
- Jupyter Notebook

---

## Dataset

Dataset used:
Telco Customer Churn Dataset

The dataset contains customer information such as:

- Customer demographics
- Services used
- Contract information
- Monthly charges
- Customer churn status

---

## ETL Process

### Extract
Loaded customer data from CSV file using Pandas.

### Transform

Performed data preprocessing:

- Converted TotalCharges column to numeric format
- Handled missing values
- Encoded categorical features

### Load

Loaded cleaned data into SQL Server database using Python and PyODBC.

---

## Machine Learning Model

Algorithm used:

Random Forest Classifier

The model was trained to classify customers into:

- 0 → Customer stays
- 1 → Customer churns

---

## Model Evaluation

Final Model Performance:

Accuracy:
77%

Classification Report:

| Class | Precision | Recall | F1-score |
|------|-----------|--------|----------|
| 0 | 0.81 | 0.90 | 0.85 |
| 1 | 0.61 | 0.41 | 0.49 |

---

## Challenges

The dataset is imbalanced because the number of retained customers is higher than churned customers.

To improve handling of imbalance:

- Used class weights in Random Forest
- Evaluated the model using precision and recall metrics

---

## Future Improvements

Possible improvements:

- Hyperparameter tuning
- Feature engineering
- SMOTE balancing technique
- Building a dashboard for business insights

---

## Author

Yasmin Ashraf