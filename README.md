# H1N1 Vaccine Prediction Machine Learning Project

## Introduction

This project focuses on building a predictive model to study the future trends of vaccine adoption, specifically for the H1N1 vaccine. The goal is to create a model that can provide insights into vaccine acceptance for public health planning.

## Domain Analysis

Before delving into data analysis, a comprehensive domain analysis was conducted to understand the significance of vaccination in public health and identify factors influencing vaccine acceptance.

## Exploratory Data Analysis (EDA)

### Tasks Performed:

- **Missing Values:** Identified and assessed columns with missing values, such as 'employment_occupation' and 'employment_industry'.
  
- **Data Types:** Examined data types to differentiate between categorical and numerical variables.

- **Balanced and Imbalanced Dataset:** Checked for class balance in target variables ('h1n1_vaccine' and 'seasonal_vaccine').

- **Univariate, Bivariate, and Multivariate Analysis:** Visualized dataset from various angles to uncover patterns and relationships.

## Data Preprocessing

### Steps Taken:

- **Handling Missing Values:** Decided to drop or impute missing values based on column significance.

- **Encoding Categorical Data:** Converted categorical columns into numerical format using techniques like Label Encoding.

- **Feature Selection:** Examined feature correlations to determine whether any features should be dropped to improve model performance.

## Model Building and Testing

Multiple machine learning models were trained, including Logistic Regression, Decision Trees, Random Forests, Support Vector Machines, Naive Bayes, K-Nearest Neighbors, Adaboost, Gradient Descent, and Stochastic Gradient Descent.

### Testing Accuracy and Training Scores:

| Model Name | Testing Accuracy H1N1 | Accuracy After HPT (H1N1) | Testing Accuracy Seasonal | Accuracy After HPT (Seasonal) |
|------------|------------------------|----------------------------|-----------------------------|--------------------------------|
| Logistic Regression | 0.6476 | 0.8335 | 0.7854 | 0.7845 |
| Decision Tree Classification | 0.5975 | 0.8337 | 0.6918 | 0.7750 |
| Naive Bayes Classification | 0.6162 | 0.7923 | 0.6821 | 0.6811 |
| K-Neighbour Classification | 0.8051 | 0.8167 | 0.7341 | 0.7615 |
| Adaboost Classification | 0.6495 | 0.8369 | 0.7869 | 0.7925 |

## Hyperparameter Tuning

Model performance was further improved through Hyperparameter Tuning (HPT), resulting in enhanced testing accuracy.

### Testing Accuracy After HPT:

| Model Name | Testing Accuracy H1N1 (After HPT) | Testing Accuracy Seasonal (After HPT) |
|------------|----------------------------------|---------------------------------------|
| Logistic Regression | 0.8335 | 0.7844 |
| Decision Tree Classification | 0.8337 | 0.7749 |
| Naive Bayes Classification | 0.7923 | 0.6811 |
| K-Neighbour Classification | 0.8167 | 0.7614 |
| Adaboost Classification | 0.8369 | 0.7925 |

## Conclusion

In conclusion, the predictive modeling efforts showed promising results in forecasting H1N1 and seasonal flu vaccine adoption. The AdaBoost classification model demonstrated the highest performance and was selected for production.

The findings can be valuable for healthcare organizations and policymakers in predicting future vaccine trends, enabling proactive vaccination campaigns and resource allocation. Further research and data collection can enhance the accuracy and robustness of the predictive models, contributing to more effective disease prevention strategies.


# Deployed Link : 
- http://vaccineprediction.pythonanywhere.com/

---