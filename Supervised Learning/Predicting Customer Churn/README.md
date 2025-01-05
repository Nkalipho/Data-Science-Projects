# Gradient Boosting Machine for Customer Churn Prediction

This project leverages the Gradient Boosting Machine (GBM) algorithm to predict customer churn in a telecommunications dataset. The primary objective is to identify customers likely to leave and help design retention strategies.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Implementation](#implementation)
- [Results](#results)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Introduction
Customer churn is a significant challenge in many industries, particularly telecommunications. By analyzing customer data, machine learning models can predict which customers are at risk of leaving, enabling businesses to take proactive measures.

This project uses Gradient Boosting Machines (GBM), a powerful ensemble learning algorithm, to build a predictive model for churn classification.

## Dataset
### Source
The dataset used is the Telco Customer Churn dataset, available on Kaggle:
[Telco Customer Churn Dataset - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Context
- **Objective**: Predict customer churn based on various features.
- **Churn**: Indicates whether a customer left within the last month.

### Content
The dataset includes:
1. **Services**: Details about phone, internet, online security, tech support, and streaming services.
2. **Account Information**: Duration of customer tenure, contract type, payment method, paperless billing, monthly charges, and total charges.
3. **Demographics**: Gender, age range, and dependency information (partners and children).

## Features
Key features include:
- **Demographic Attributes**: `gender`, `age`, `partner`, `dependents`
- **Account Attributes**: `tenure`, `contract`, `payment_method`, `monthly_charges`, `total_charges`
- **Service Attributes**: `phone_service`, `internet_service`, `online_security`, `tech_support`, `streaming_tv`

The target variable is **`Churn`**: binary (1 for churned, 0 for retained).

## Implementation
1. **Preprocessing**:
   - Handled missing values.
   - Encoded categorical variables using techniques like one-hot encoding.
   - Scaled numerical variables for uniformity.

2. **Model Selection**:
   - Chose Gradient Boosting Machine for its robustness in handling imbalanced datasets.

3. **Training**:
   - Split the dataset into training and testing subsets.
   - Trained the model using Gradient Boosting in `scikit-learn`.

4. **Evaluation**:
   - Used metrics such as accuracy, precision, recall, and F1-score to evaluate the model.

## Results
The Gradient Boosting Machine achieved:
- **Accuracy**: 73%
- **Precision**: Moderate
- **Recall**: Moderate
- **F1-Score**: Balanced performance across classes

While the results are promising, there is room for improvement through hyperparameter tuning and feature engineering.

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the training script:
   ```bash
   python churn_prediction.py
   ```
4. View results and evaluation metrics in the terminal or generated output files.

## Conclusion
This project demonstrates the utility of Gradient Boosting Machines for customer churn prediction. Future enhancements may include:
- Testing with other advanced algorithms like XGBoost or CatBoost.
- Incorporating external data for additional insights.
- Deploying the model into a web application for real-time predictions.

---
For further questions or contributions, feel free to contact me or open a pull request!

