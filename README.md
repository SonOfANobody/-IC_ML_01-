🌦 Project Title: Weather Temperature Forecasting Project
📌 Overview

This project builds a machine learning pipeline to predict ambient temperature using historical weather data. The solution includes feature engineering, preprocessing, model tuning, and deployment.

📌 Objectives

Predict future weather parameters

Analyze seasonal and trend patterns

Compare traditional and deep learning forecasting models

🧠 Features
Time-series data preprocessing

Data visualization and trend analysis

Datetime feature extraction (hour, day, month, season)

Lag features for temporal dependency

Robust preprocessing with pipelines

Hyperparameter tuning using GridSearchCV

Model explainability via feature importance

Regression-based forecasting

Model performance evaluation

🏗 Models Used

Linear Regression (baseline)

Random Forest Regressor (tuned)

📊 Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

Technologies Used

Python

Pandas, NumPy

Matplotlib

Scikit-learn

TensorFlow / Keras


🚀 How to Run
pip install -r requirements.txt
streamlit run app.py

📁 Project Structure
├── app.py
├── weather_temperature_model.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
