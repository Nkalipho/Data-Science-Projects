# Email Spam Detection Project

This project focuses on building a spam detection system using the Naive Bayes algorithm. The primary goal is to classify emails as spam or non-spam based on their content and features. 

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Implementation](#implementation)
- [Results](#results)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Introduction
Spam emails are a persistent issue in the digital world, and an efficient spam detection system is crucial for filtering out unwanted emails. Using the Naive Bayes algorithm, this project classifies emails based on the likelihood of them being spam or not.

## Dataset
The dataset used in this project is the Spambase dataset, available at the UCI Machine Learning Repository. 

- The dataset contains features extracted from email headers and bodies.
- The classification task is to determine whether an email is spam or non-spam.

### Dataset Source
The "spam" concept includes diverse categories: advertisements, chain letters, and more. The data was collected from spam emails reported by individuals and non-spam emails from work and personal correspondence. 

For more details and to access the dataset, visit: [Spambase Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/94/spambase)

## Features
The dataset includes 57 features, such as:
- Word frequencies: e.g., `word_freq_make`, `word_freq_address`
- Character frequencies: e.g., `char_freq_$`, `char_freq_!`
- Capital letter usage: e.g., `capital_run_length_average`, `capital_run_length_total`

The target variable is a binary label indicating whether an email is spam (`1`) or not (`0`).

## Implementation
1. **Preprocessing:**
   - Converted the dataset into a format compatible with the Naive Bayes classifier.
   - Normalized and cleaned the data.

2. **Model Building:**
   - Implemented a Gaussian Naive Bayes classifier using `scikit-learn`.
   - Split the dataset into training and testing sets.

3. **Evaluation:**
   - Evaluated the model's performance using metrics like accuracy, precision, recall, and F1-score.
   - Conducted hyperparameter tuning for optimal performance.

## Results
The Naive Bayes classifier achieved:
- **Accuracy:** 82%
- **Precision:** 85%
- **Recall:** 82%
- **F1-Score:** 82%

The results demonstrate the model's effectiveness in identifying spam emails while maintaining a low false positive rate.

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
3. Run the script:
   ```bash
   python spam_detection.py
   ```
4. View the results in the terminal or the generated output files.

## Conclusion
The project demonstrates the efficacy of the Naive Bayes algorithm in spam detection tasks. Future improvements include testing on larger datasets and implementing other machine learning algorithms for comparison.

---
For any questions or contributions, feel free to contact me or submit a pull request!

