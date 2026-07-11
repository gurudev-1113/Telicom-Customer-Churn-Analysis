# Customer Churn Prediction with Deployment 🚀

An end-to-end Machine Learning project to predict customer churn using **Scikit-learn, XGBoost, MLflow, FastAPI, Docker, and AWS deployment**.

## 📌 Project Overview

Customer churn prediction helps organizations identify customers who are likely to leave their services. This project builds a complete ML pipeline that analyzes customer behavior, trains machine learning models, tracks experiments using MLflow, and deploys the final prediction model as a REST API.

The deployed API allows users to send customer details and receive real-time churn predictions.

---

# 🏗️ Project Workflow

```
Data Collection
        |
Data Cleaning
        |
Exploratory Data Analysis (EDA)
        |
Feature Engineering
        |
Model Training
        |
Hyperparameter Tuning
        |
Model Evaluation
        |
MLflow Experiment Tracking
        |
FastAPI REST API
        |
Docker Containerization
        |
AWS Cloud Deployment
```

---

# 🛠️ Tech Stack

## Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost

## Model Tracking

* MLflow

## API Development

* FastAPI
* Pydantic

## Deployment

* Docker
* AWS Elastic Beanstalk
* AWS S3

---

# 🤖 Models Implemented

The following classification algorithms were trained and compared:

* Logistic Regression
* Random Forest Classifier
* XGBoost Classifier

## Evaluation Metrics

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

XGBoost was selected as the final model due to its strong performance.

---

# 🚀 Running the Application

## 1. Clone Repository

```bash
git clone <repository-url>

cd Customer-Churn-Prediction-with-Deployment
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🐳 Docker Deployment

Build Docker image:

```bash
docker build -t churn-api -f docker/Dockerfile .
```

Run container:

```bash
docker run -p 8000:8000 churn-api
```

The API will be available at:

```
http://localhost:8000
```

Swagger API Documentation:

```
http://localhost:8000/docs
```

---

# 🔮 API Prediction Example

### Request

```json
{
  "CreditScore":650,
  "Geography":"France",
  "Gender":"Male",
  "Age":40,
  "Tenure":5,
  "Balance":60000,
  "NumOfProducts":2,
  "HasCrCard":1,
  "IsActiveMember":1,
  "EstimatedSalary":50000,
  "Complain":0,
  "SatisfactionScore":4,
  "CardType":"Gold",
  "PointEarned":500
}
```

### Response Example

```json
{
  "prediction": "Customer will not churn",
  "probability": 0.12
}
```

---

# 📂 Project Structure

```
Customer-Churn-Prediction-with-Deployment

│
├── api/
│   ├── main.py
│   ├── schema.py
│
├── model/
│   └── churn_pipeline.pkl
│
├── notebook/
│   └── Customer_Churn_Model.ipynb
│
├── docker/
│   └── Dockerfile
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# 📊 MLflow Tracking

MLflow is used for:

* Experiment tracking
* Parameter logging
* Metric logging
* Model version management

---

# ☁️ Deployment Architecture

```
User
 |
FastAPI Endpoint
 |
Docker Container
 |
AWS Elastic Beanstalk
 |
ML Model
 |
Prediction Response
```

---

# 🔮 Future Improvements

* Deploy complete application on AWS Elastic Beanstalk
* Store model artifacts using AWS S3
* Add CI/CD pipeline using GitHub Actions
* Add model monitoring and drift detection

---

# 👨‍💻 Author

**Gurudev**

Data Science | Machine Learning | Backend Deployment
