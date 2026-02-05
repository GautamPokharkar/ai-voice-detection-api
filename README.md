🎙️ AI-Generated Voice Detection – API Service

A lightweight API-based voice analysis system built using FastAPI, designed to detect whether a given voice sample is AI-generated or human-generated using machine-learning–based acoustic analysis.

✅ Features

REST API for AI vs Human voice classification

Accepts Base64-encoded MP3 audio

Supports multiple languages:

Tamil

English

Hindi

Malayalam

Telugu

ML-based prediction with confidence score

Human-readable explanation for each decision

Stable, deterministic, and evaluation-ready API

📄 API Overview
Endpoint	Description
/api/voice-detection	Classifies voice input as AI-generated or human-generated
🧠 Detection Approach

Machine-learning–based classification

Audio features extracted using librosa

Feature set includes:

MFCC statistical features

Spectral contrast characteristics

Pitch variability

Zero-crossing rate

Language-aware normalization applied for Indian languages

A pre-trained RandomForest classifier is used for inference

Model is trained offline and loaded at runtime for fast predictions

⚠️ Training data is intentionally excluded from this repository.

📥 Input

Audio format: MP3

Encoding: Base64

Language metadata: Required in request body

Example Request
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "<BASE64_ENCODED_AUDIO>"
}

📤 Output
Example Response
{
  "status": "success",
  "language": "Tamil",
  "classification": "HUMAN",
  "confidence": 0.94,
  "confidenceScore": 0.94,
  "explanation": "Natural voice variations observed"
}

Output Fields
Field	Description
classification	AI_GENERATED or HUMAN
confidence	Model confidence score (0.0 – 1.0)
explanation	Reasoning behind the prediction
🔐 Authentication

All API requests require an API key passed via headers:

x-api-key: sk_test_123456789

🧪 Local Execution

Start the API server:

uvicorn app:app --reload


Server runs at:

http://127.0.0.1:8000

🧠 Model Details

Feature extraction: librosa, NumPy

Classifier: RandomForest (scikit-learn)

Model file:

model/artifacts/voice_classifier.pkl


Model is loaded once at startup for low-latency inference

🧰 Tech Stack

Language: Python

Framework: FastAPI

Audio Processing: librosa, NumPy

Machine Learning: scikit-learn

Authentication: API key via request headers

🎯 Learning Outcomes

Built an end-to-end ML-powered voice detection system

Applied speech signal processing techniques for AI detection

Implemented language-aware acoustic normalization

Designed an explainable ML inference API

Gained experience deploying evaluation-ready AI services

