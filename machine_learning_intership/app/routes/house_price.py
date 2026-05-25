from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from machine_learning_intership.app.ml.house_price_model import predict_price

router = APIRouter(tags=["House Price Prediction"], prefix="/house-price")


class HousePriceRequest(BaseModel):
    location: str = Field(example="Whitefield")
    bhk: int = Field(..., gt=0, example=2)
    total_sqft: int = Field(..., gt=0, example=1200)
    bath: int = Field(..., gt=0, example=2)
    balcony: int = Field(..., ge=0, example=1)


@router.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


@router.post("/predict")
def predict_house_price(request: HousePriceRequest):
    try:
        predicted_price = predict_price(
            location=request.location,
            bhk=request.bhk,
            total_sqft=request.total_sqft,
            bath=request.bath,
            balcony=request.balcony
        )

        return {
            "location": request.location,
            "bhk": request.bhk,
            "total_sqft": request.total_sqft,
            "bath": request.bath,
            "balcony": request.balcony,
            "predicted_price_lakhs": predicted_price
        }

    except Exception as error:
        raise HTTPException(status_code=500,detail=f"Prediction failed: {str(error)}")