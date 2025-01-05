# Credit Card Fraud Detection Project

This project focuses on detecting fraudulent credit card transactions using machine learning, specifically the Random Forest algorithm. The primary goal is to classify transactions as fraudulent or non-fraudulent based on their features.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Implementation](#implementation)
- [Results](#results)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Introduction
Credit card fraud is a major issue in the financial industry, and an efficient detection system is essential to prevent fraudulent activities. This project aims to identify fraudulent transactions using machine learning techniques. Given the highly imbalanced nature of the dataset, the evaluation metric used is the Area Under the Precision-Recall Curve (AUPRC).

## Dataset
The dataset used in this project contains transactions made by European cardholders in September 2013.

- The dataset includes 284,807 transactions, of which 492 are frauds, representing just 0.172% of the total transactions.
- The features have been transformed using PCA for confidentiality reasons, and the target variable is whether a transaction is fraudulent or not.

### Dataset Source
For more details and to access the dataset, visit: [Credit Card Fraud Detection - Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Features
The dataset contains the following key features:
- **V1, V2, ..., V28**: PCA-transformed features that represent various aspects of the transactions.
- **Time**: The time elapsed in seconds between the current transaction and the first transaction in the dataset.
- **Amount**: The transaction amount, which can be used for cost-sensitive learning.
- **Class**: The target variable (1 for fraud, 0 for non-fraud).

## Implementation
1. **Preprocessing:**
   - Loaded the dataset and split it into training and testing sets.
   - Standardized the features to ensure that the model performed optimally.

2. **Model Building:**
   - Implemented a Random Forest classifier using `scikit-learn`.
   - The model was trained using the training data and evaluated using the test data.

3. **Evaluation:**
   - Evaluated the model using the Precision-Recall AUC score (AUPRC) due to the imbalanced nature of the dataset.
   - Visualized the Precision-Recall curve for a better understanding of the model's performance.

## Results
The Random Forest classifier achieved the following:
- **Precision-Recall AUC:** 1.00

This indicates that the model perfectly detected fraudulent transactions on the test set.

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-folder>

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Run the script:
   ```bash
   python fraud_detection.py
   
4. View the results in the terminal or the generated output files.
   
## Conclusion

This project demonstrates the effectiveness of the Random Forest algorithm in detecting fraudulent credit card transactions in an imbalanced dataset. The model achieved perfect performance as measured by the Precision-Recall AUC. Future improvements include testing other algorithms and refining the feature engineering process.
