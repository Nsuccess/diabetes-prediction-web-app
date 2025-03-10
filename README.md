# diabetes-prediction-web-app
**Diabetes Prediction Web App**  This Streamlit-powered app predicts the likelihood of diabetes based on user-provided health indicators. It utilizes a trained machine learning model and offers a user-friendly interface for quick and easy predictions.    For detailed information, please refer to the README.

# Diabetes Prediction Web App

## Overview

This web application provides a user-friendly interface to predict the likelihood of diabetes based on user inputs. It leverages a machine learning model trained on the Pima Indians Diabetes Dataset and is built using Streamlit.

## Features

- **Intuitive Input:** Easily enter eight key health indicators.
- **Instant Prediction:** Get real-time predictions of diabetes risk.
- **User-Friendly:**  Simple and easy to navigate for all users.
- **Deployable:** Can be easily deployed for broader access.

## How it works

1. **User Input:** The app takes eight health indicators as input:
    - Pregnancies
    - Glucose
    - Blood Pressure
    - Skin Thickness
    - Insulin
    - BMI
    - Diabetes Pedigree Function
    - Age
2. **Prediction:** A pre-trained Support Vector Machine (SVM) model analyzes the input data.
3. **Output:** The app displays the prediction, indicating the likelihood of diabetes.

## Getting Started

1. **Clone:** `git clone https://github.com/Nsuccess/diabetes-prediction-web-app.git`
2. **Install:** `pip install -r requirements.txt`
3. **Run:** `streamlit run app.py`

## Dataset

The model was trained using the [Pima Indians Diabetes Dataset](https://www.google.com/url?q=https%3A%2F%2Fwww.dropbox.com%2Fscl%2Ffi%2F4mqx40cvbqjrt8oa4ghcq%2Fdiabetes.csv%3Frlkey%3Dwtckz2bgujl7yo6tfchwrkbii%26st%3Dphnm3lqu%26dl%3D0). This dataset is publicly available...

## Model

The prediction model is a Support Vector Machine (SVM), known for its effectiveness in classification tasks.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.
