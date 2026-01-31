# 🎙️ AI-Generated Voice Detection – API Service

A lightweight **API-based voice analysis system** built using **FastAPI**, designed to detect whether a given voice sample is **AI-generated or human-generated** using acoustic feature analysis.

---

## ✅ Features

- REST API for AI vs Human voice classification  
- Accepts **Base64-encoded MP3 audio**  
- Supports **multiple languages** (Tamil, English, Hindi, Malayalam, Telugu)  
- Confidence-scored predictions with human-readable explanations  
- Stable, deterministic, and evaluation-ready  

---

## 📄 API Overview

| Endpoint               | Description                                         |
|------------------------|-----------------------------------------------------|
| `/api/voice-detection` | Classifies voice input as AI-generated or human     |

---

## 🧠 Detection Approach

- **Heuristic-based voice analysis** (no trained ML/DL model)  
- **librosa** used strictly for audio feature extraction  
- MFCC variance used to measure spectral consistency  
- Spectral flatness used to detect uniform frequency patterns  
- Rule-based logic combines features to estimate AI likelihood  

---

## 📥 Input

- Audio format: MP3  
- Encoding: Base64  
- Language metadata included in the request  

---

## 📤 Output

- Classification: `AI` or `Human`  
- Confidence score (`0.0 – 1.0`) indicating likelihood of AI-generated voice  
- Clear explanation describing the decision  

---

## 🎯 Learning Outcomes

- Designed a **heuristic-based AI detection pipeline**  
- Applied **speech signal processing concepts** for voice analysis  
- Built a **secure and stable FastAPI service** with authentication  
- Learned to generate **explainable AI outputs**  

---

## 🧰 Tech Stack

- **Language:** Python  
- **Framework:** FastAPI  
- **Audio Processing:** librosa, NumPy  
- **Authentication:** API key via request headers  

---


