# Credit Card Fraud Detection

This project involves detecting fraudulent credit card transactions using a dataset of transactions made by European cardholders. The dataset contains transactions from September 2013, where there were 492 frauds out of 284,807 transactions. The fraud class accounts for only 0.172% of the total transactions, making the dataset highly imbalanced.

The goal is to detect fraudulent transactions using machine learning, and the model accuracy is measured using the **Area Under the Precision-Recall Curve (AUPRC)**, which is more suitable for unbalanced datasets than traditional accuracy or confusion matrix metrics.

## Dataset Overview

The dataset consists of the following features:

- **V1, V2, ..., V28**: Principal components obtained via PCA transformation (no raw feature names due to confidentiality).
- **Time**: The time elapsed in seconds between each transaction and the first transaction in the dataset.
- **Amount**: The transaction amount, which may be used for example-dependent cost-sensitive learning.
- **Class**: The target variable. 1 indicates a fraud, and 0 indicates a non-fraud.

## Model Overview

### Algorithm
- **Random Forest Classifier**: A powerful ensemble learning method that works well with imbalanced datasets.

### Evaluation Metric
- **Area Under the Precision-Recall Curve (AUPRC)**: Since the dataset is highly imbalanced, the model's performance is best evaluated using the Precision-Recall curve, rather than traditional accuracy.

## Steps Involved

1. **Data Preprocessing**: 
   - Handle missing values (if any).
   - Split data into training and test sets.
   - Normalize or standardize features as necessary.

2. **Model Training**: 
   - Train a Random Forest model using the training data.

3. **Model Evaluation**:
   - Evaluate the model using the Precision-Recall AUC score (AUPRC).
   - Display confusion matrix for further insights.

4. **Model Tuning**:
   - Experiment with hyperparameters to improve model performance (e.g., `n_estimators`, `max_depth`, `min_samples_split`).

## Installation

To run this project, you'll need the following libraries:

```bash
pip install pandas numpy scikit-learn matplotlib
