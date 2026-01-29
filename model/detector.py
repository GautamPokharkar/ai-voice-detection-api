import librosa
import numpy as np

def detect_ai_voice(y, sr):
    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_variance = np.var(mfcc)

    # Normalize confidence (simple heuristic)
    confidence = min(mfcc_variance / 15000, 1.0)

    if confidence > 0.6:
        classification = "AI_GENERATED"
        explanation = "Unnatural spectral consistency detected"
    else:
        classification = "HUMAN"
        explanation = "Natural voice variations observed"

    return classification, round(confidence, 2), explanation
