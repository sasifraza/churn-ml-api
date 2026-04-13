from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title= "Churn Prediction API")

class ChurnRequest(BaseModel):
    tenure: float
    monthly_charges: float
    total_charges: float


@app.get("/")
def home():
    return{"message": "Churn API is running"}

@app.post("/predict")

def predict(data:ChurnRequest):
    # temporary dummy logic 
    score  = data.monthly_charges/(data.tenure +1)

    prediction = 1 if score > 50 else 0

    return{
        "churn_prediction" : prediction,
        "score" : score
    }

