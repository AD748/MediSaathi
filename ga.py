import wave
import numpy as np

sample_rate = 16000
duration = 2
frequency = 440

t = np.linspace(0, duration, int(sample_rate * duration))
audio = (0.5 * np.sin(2 * np.pi * frequency * t)).astype(np.float32)

with wave.open("sample.wav", "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes((audio * 32767).astype(np.int16).tobytes())