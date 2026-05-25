from fastapi import FastAPI

from machine_learning_intership.app.routes.house_price import router

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting Bengaluru house prices using a trained ML model",
    version="1.0.0"
)


app.include_router(router)