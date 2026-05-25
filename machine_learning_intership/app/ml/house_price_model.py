import joblib
import json
import pandas as pd

model = joblib.load('D:/Product Projects/ml-internship/machine_learning_intership/trained_models/house_price_prediction_model.pkl')
with open("D:/Product Projects/ml-internship/machine_learning_intership/trained_models/house_price_features.json", "r") as f:
    feature_names = json.load(f)

def predict_price(location: str, bhk:int, total_sqft:int, bath:int, balcony:int):
    input_data = pd.DataFrame([{col:0 for col in feature_names}])
    input_data['bhk'] = bhk
    input_data['total_sqft'] = total_sqft
    input_data['bath'] = bath
    input_data['balcony'] = balcony

    location_col = f"location_{location}"
    if location_col in input_data.columns:
        input_data[location_col] = 1

    prediction = model.predict(input_data)
    return round(float(prediction[0]), 2)