# model/train_model.py
import os
import joblib
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from model.feature_extractor import extract_features

DATASET = [
    # ("path/to/audio.mp3", "English", 1),  # AI
    # ("path/to/audio.mp3", "Tamil", 0),    # Human
]

X, y = [], []

for audio_path, language, label in DATASET:
    audio, sr = librosa.load(audio_path, sr=None)
    features = extract_features(audio, sr, language)
    X.append(features)
    y.append(label)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

os.makedirs("model/artifacts", exist_ok=True)
joblib.dump(model, "model/artifacts/voice_classifier.pkl")

print("✅ Model trained and saved")
