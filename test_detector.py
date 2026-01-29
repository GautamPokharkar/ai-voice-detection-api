import librosa
from model.detector import detect_ai_voice

# load audio
y, sr = librosa.load("data/sample.mp3", sr=None)

# call your function
result = detect_ai_voice(y, sr)
print(result)
