import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"
preprocessor = joblib.load(PREPROCESSOR_PATH)
try:
    print(preprocessor.named_transformers_['cat'].categories_)
except Exception as e:
    print(e)
