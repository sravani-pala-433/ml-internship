from fastapi import FastAPI

from machine_learning_intership.app.routes.house_price import router
from machine_learning_intership.app.routes.spam_classifier import router as spam_router
app = FastAPI(
    title="Machine Learning Internship",
    version="1.0.0"
)

app.include_router(router)

app.include_router(spam_router)