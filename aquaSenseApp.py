from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="AquaSense AI", description="Smart Water Quality & Flood Risk Prediction API")

class SensorData(BaseModel):
    ph: float
    turbidity: float
    temperature: float
    rainfall_mm: float

@app.get("/")
def root():
    return {"message": "￼ AquaSense AI API is running successfully!"}

@app.post("/predict")
def predict(data: SensorData):
    # Simple AI-based rule logic (placeholder for ML model)
    risk_score = (data.turbidity * 0.3 + data.rainfall_mm * 0.4 + (7 - abs(7 - data.ph)) * 0.3)
    flood_risk = "High" if risk_score > 6 else "Medium" if risk_score > 4 else "Low"

    # Random water safety index for demo
    water_quality_index = round(random.uniform(60, 95), 2)

    return {
        "Flood_Risk_Level": flood_risk,
        "Water_Quality_Index": water_quality_index,
        "AI_Score": round(risk_score, 2),
        "Message": "Prediction generated successfully."
    }
