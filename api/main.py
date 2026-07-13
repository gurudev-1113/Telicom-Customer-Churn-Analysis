from fastapi import FastAPI
from api.schema import CustomerData
import joblib
import pandas as pd
from mangum import Mangum
from main import app

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
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best_xgboost_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)
@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API",
        "status": "Running"
    }

@app.post("/predict")
def predict(customer: CustomerData):

    data = pd.DataFrame([customer.model_dump()])
    
    # Map Gender to int if it's a string, assuming Male=1, Female=0
    if 'Gender' in data.columns:
        data['Gender'] = data['Gender'].map({"Male": 1, "Female": 0}).fillna(data['Gender'])
        # If it was already int, fillna keeps it. 
        # But let's make sure it's int or at least not fail if unknown
        data['Gender'] = pd.to_numeric(data['Gender'], errors='coerce').fillna(1).astype(int)
        
    # Ensure CardType is uppercase as expected by OneHotEncoder
    if 'CardType' in data.columns:
        data['CardType'] = data['CardType'].astype(str).str.upper()

    transformed = preprocessor.transform(data)

    prediction = model.predict(transformed)[0]

    probability = model.predict_proba(transformed)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 4)
    }
handler = Mangum(app)