#predict

import joblib
from feature_extraction import extract_features

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_image(image_path):
    features, intensity, contrast, edge_density = extract_features(image_path)

    features = scaler.transform([features])

    prob = model.predict_proba(features)[0][1]
    prediction = "Stroke Risk" if prob > 0.5 else "Normal"

    return prediction, prob, intensity, contrast, edge_density