# Predicting House Prices Project

This project focuses on predicting house prices using machine learning algorithms. By analyzing historical data, the goal is to build a model capable of estimating the market value of homes based on various features.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Features](#features)
- [Implementation](#implementation)
- [Results](#results)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Introduction
Accurately predicting house prices is crucial for buyers, sellers, and real estate professionals. This project leverages supervised machine learning techniques to provide reliable price estimates based on factors such as location, size, and amenities.

## Dataset
The dataset used in this project is sourced from [Kaggle's House Price Competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques). It includes features such as:
- Lot size
- Square footage
- Number of bedrooms and bathrooms
- Location and neighborhood details

### Dataset Highlights
- **Rows:** 1460 (training data)
- **Columns:** 81 (including categorical and numerical features)
- **Target Variable:** Sale price of the house

## Features
The dataset contains:
1. **Numerical Features:**
   - Lot area
   - Gr living area
   - Garage area
2. **Categorical Features:**
   - Neighborhood
   - House style
   - Sale condition

## Implementation
1. **Data Preprocessing:**
   - Handled missing values.
   - Encoded categorical variables using one-hot encoding.
   - Scaled numerical features for model compatibility.

2. **Modeling:**
   - Implemented regression algorithms such as Linear Regression, Random Forests, and Gradient Boosting Machines.
   - Performed hyperparameter tuning using Grid Search and Cross-Validation.

3. **Evaluation:**
   - Assessed model performance using metrics such as R² and Mean Absolute Error (MAE).

## Results
- **Best Model:** Simple Linear Regression
- **R² Score:** 0.60
- **MAE:** $12,300

The model successfully captured the key factors influencing house prices and achieved high accuracy on the test dataset.

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
3. Open the notebook:
   ```bash
   jupyter notebook Predicting_House_Prices.ipynb
   ```
4. Follow the steps in the notebook to preprocess the data, train models, and evaluate results.

## Conclusion
This project demonstrates the power of machine learning in real estate pricing. Future work includes:
- Incorporating more datasets to improve generalizability.
- Testing additional algorithms like XGBoost and CatBoost.

---
For any questions or suggestions, feel free to contact me or submit a pull request!

