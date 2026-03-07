from services.speech_to_text.whisper_stt import transcribe

with open("sample.wav", "rb") as f:
    audio = f.read()

print("Audio size:", len(audio))

text = transcribe(audio)

print("Transcription:", text)