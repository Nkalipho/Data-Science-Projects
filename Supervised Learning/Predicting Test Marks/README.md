# Predicting Test Marks

This project aims to predict students' test marks based on various features like study hours, attendance, and prior academic performance. By leveraging machine learning techniques, we aim to provide accurate predictions and insights for academic improvement.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Implementation](#implementation)
- [Results](#results)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Introduction
Understanding the factors influencing academic performance can significantly help students, educators, and institutions. This project applies machine learning to predict test scores, offering actionable insights to improve student outcomes.

## Dataset
The dataset used in this project contains information about students' academic behaviors and test marks.

- **Columns include:**
  - `Study Hours`: Number of hours spent studying.
  - `Attendance`: Percentage of classes attended.
  - `Past Performance`: Average marks from previous exams.
  - `Test Marks`: Target variable representing the marks scored.

### Data Source
The dataset is synthetic and created for academic purposes. Ensure you preprocess the dataset properly to remove any anomalies or missing values.

## Features
- **Input Features:**
  - `Study Hours`
  - `Attendance`
  - `Past Performance`
- **Target Feature:**
  - `Test Marks`

## Implementation
1. **Data Preprocessing:**
   - Handled missing values and normalized the data.
   - Split the dataset into training and testing sets.

2. **Model Selection:**
   - Tested multiple models such as Linear Regression, Decision Trees, and Random Forest.

3. **Training and Testing:**
   - Trained models on the training set and evaluated their performance using the testing set.

4. **Evaluation Metrics:**
   - Used metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²) to evaluate performance.

## Results
The best-performing model achieved:
- **Mean Absolute Error (MAE):** 3.5
- **Mean Squared Error (MSE):** 12.8
- **R-squared (R²):** 0.89

These results indicate that the model provides reliable predictions for students' test marks.

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
3. Run the notebook:
   ```bash
   jupyter notebook Predicting_Test_Marks.ipynb
   ```
4. Follow the steps in the notebook to preprocess data, train the model, and evaluate results.

## Conclusion
This project successfully demonstrates the use of machine learning for predicting test marks. By analyzing key features like study hours and attendance, educators and students can identify areas for improvement and enhance academic performance.

---
Feel free to reach out for any questions or contributions!

