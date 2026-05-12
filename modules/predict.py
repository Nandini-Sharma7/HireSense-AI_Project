import joblib

# Load trained model
model = joblib.load("ml_model/model.pkl")

def predict_resume_category(resume_text):

    prediction = model.predict([resume_text])

    return prediction[0]