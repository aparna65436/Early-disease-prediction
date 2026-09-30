# 🩺 Early Disease Prediction

An AI/ML-based web application that predicts diabetes risk using health-related parameters and a trained Random Forest classification model.

## 📌 About the Project

Early Disease Prediction is a machine learning project developed to demonstrate how health-related data can be used to estimate diabetes risk.

The project uses the **Pima Indians Diabetes Dataset** and a **Random Forest Classifier** to make predictions based on 8 input features.

The trained model is integrated into a **Streamlit web application**, allowing users to enter health information and receive a predicted diabetes-risk result.

## 🎯 Objective

The main objectives of this project are:

* To build a machine learning model for diabetes risk prediction.
* To compare machine learning approaches during model development.
* To use Random Forest for the final prediction system.
* To create an interactive web interface using Streamlit.
* To display the model's predicted risk probability.

## 🤖 Machine Learning

### Final Model

**Random Forest Classifier**

The model was trained using:

* Number of trees: 100
* Random state: 42

### Input Features

The model uses the following 8 features:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

### Output

The model predicts:

* Lower diabetes risk
* Higher diabetes risk

The application also displays the model's estimated diabetes-risk probability.

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **Streamlit**
* **Jupyter Notebook**
* **Git & GitHub**

## 📂 Project Structure

```text
Early-disease-prediction/
│
├── data/
│   └── diabetes.csv
│
├── app.py
├── model.pkl
├── early_disease_prediction.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/aparna65436/Early-disease-prediction.git
```

### 2. Open the project folder

```bash
cd Early-disease-prediction
```

### 3. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install the required libraries

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Model Development

The machine learning model was developed and evaluated in the Jupyter Notebook:

`early_disease_prediction.ipynb`

The workflow includes:

```text
Dataset
   ↓
Data Preparation
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Random Forest Selection
   ↓
Model Serialization
   ↓
Streamlit Application
```

## ⚠️ Disclaimer

This application is an educational machine learning project. Its predictions are not a medical diagnosis and should not be used as a substitute for professional medical advice.

## 🚀 Future Improvements

* Add additional disease prediction models.
* Improve the user interface.
* Add model performance visualizations.
* Add more comprehensive input validation.
* Deploy the application for public access.
* Improve model calibration and evaluation using additional metrics.
* Explore explainable AI techniques to help understand model predictions.

## 👩‍💻 Author

**Aparna Singh**

GitHub: [@aparna65436](https://github.com/aparna65436)
