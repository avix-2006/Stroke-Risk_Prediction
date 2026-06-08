NeuroVision AI: Stroke Risk Prediction Using Retinal Fundus Image
Overview
NeuroVision AI is an intelligent healthcare application designed to predict stroke risk from retinal fundus
images using machine learning and image processing techniques. The system analyzes retinal
characteristics, extracts relevant image features, and classifies the likelihood of stroke risk. A
user-friendly web interface enables image upload, risk assessment, visualization of extracted features, and
automatic PDF report generation.
Features
- Retinal fundus image upload and analysis
- Automated image preprocessing and feature extraction
- Stroke risk prediction using Logistic Regression
- Extraction of retinal image metrics such as intensity, contrast, and edge density
- Real-time prediction results through a web dashboard
- Dynamic PDF medical report generation
- Interactive and user-friendly Flask-based interface
Technologies Used
1. Programming Language
- Python
2. Machine Learning
- Scikit-learn
- Logistic Regression (L1-Regularized)
3. Image Processing
- OpenCV
- NumPy
4. Web Framework
- Flask
5. Report Generation
- ReportLab
6. Model Serialization
- Joblib
7. Frontend
- HTML
- CSS
Methodology
1. Image Acquisition
Retinal fundus images are uploaded through the web interface.
2. Image Preprocessing
Images undergo resizing, normalization, and enhancement to improve feature extraction quality.
3. Feature Extraction
Important retinal characteristics such as intensity, contrast, and edge density are extracted from the
uploaded image.
4. Feature Scaling
Extracted features are normalized using a pre-trained scaler to ensure consistent model input.
5. Stroke Risk Prediction
The processed features are passed to an L1-Regularized Logistic Regression classifier, which predicts
the probability of stroke risk.
6. Result Visualization
Prediction results and extracted feature values are displayed on the dashboard.
7. Report Generation
A dynamic PDF report containing prediction results, extracted features, and clinical interpretation is
generated for download.
Project Structure
NeuroVision-AI/
│
├── app.py
├── predict.py
├── feature_extraction.py
├── report.py
├── model.pkl
├── scaler.pkl
│
├── static/
│ ├── uploads/
│ └── reports/
│
├── templates/
│ └── index.html
Conclusion
The project demonstrates an efficient approach for stroke risk prediction using retinal fundus images. By
combining CNN-based deep features with handcrafted retinal features and applying L1-regularized
Logistic Regression, the system achieves a balance between prediction performance and interpretability.
The developed solution provides an automated framework for retinal image analysis and stroke-risk
assessment.
