from fastapi import FastAPI
from api.schema import CustomerData
import joblib
import pandas as pd

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and preprocessor once when the app starts
model = joblib.load("models/best_xgboost_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API",
        "status": "Running"
    }

@app.post("/predict")
def predict(customer: CustomerData):

    data = pd.DataFrame([customer.model_dump()])

    transformed = preprocessor.transform(data)

    prediction = model.predict(transformed)[0]

    probability = model.predict_proba(transformed)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 4)
    }