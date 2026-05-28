import joblib

model = joblib.load('D:/Product Projects/ml-internship/machine_learning_intership/trained_models/spam_classifier_model.pkl')
tfidf = joblib.load('D:/Product Projects/ml-internship/machine_learning_intership/trained_models/spam_classifier_tfidf_vectorizer.pkl')

def spam_prediction(message: str):
    message_vector = tfidf.transform([message])
    prediction = model.predict(message_vector)
    probability = model.predict_proba(message_vector)

    return {
        "message": message,
        "prediction" : "Spam" if prediction[0] == 1 else "Not Spam",
        "spam_probability": probability[0][1] * 100 if prediction[0] == 1 else 0,
        "not_spam_probability": probability[0][0] * 100 if prediction[0] == 0 else 0
    }

