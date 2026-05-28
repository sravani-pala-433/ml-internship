from fastapi import APIRouter
from pydantic import BaseModel
from machine_learning_intership.app.ml.spam_model import spam_prediction
router = APIRouter(tags=["Spam Classifier"])

class MessageInput(BaseModel):
    message: str

@router.post("/predict-spam")
def predict_spam(input: MessageInput):
    result = spam_prediction(input.message)
    return result