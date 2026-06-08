import cv2
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# CNN model
cnn_model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')


def extract_cnn_features(img):
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    features = cnn_model.predict(img, verbose=0)
    return features.flatten()


def extract_manual_features(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    intensity = np.mean(gray)
    contrast = np.std(gray)

    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.sum(edges > 0) / edges.size

    return intensity, contrast, edge_density


def extract_features(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found")

    cnn_features = extract_cnn_features(img)
    intensity, contrast, edge_density = extract_manual_features(img)

    fused_features = np.hstack([cnn_features, [intensity, contrast, edge_density]])

    return fused_features, intensity, contrast, edge_density