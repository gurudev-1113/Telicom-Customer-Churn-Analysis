from api.schema import CustomerData
import pandas as pd
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "best_xgboost_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

print("Loading models...")
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)
print("Models loaded successfully.")

customer_dict = {
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

customer = CustomerData(**customer_dict)

print("Predicting...")
data = pd.DataFrame([customer.model_dump()])
print(data)

transformed = preprocessor.transform(data)
print("Transformed data:")
print(transformed)

prediction = model.predict(transformed)[0]
probability = model.predict_proba(transformed)[0][1]

print("Prediction:", prediction)
print("Probability:", probability)
