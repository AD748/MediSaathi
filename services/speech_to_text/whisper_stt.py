import whisper
import tempfile
import os

# load model once at startup
model = whisper.load_model("tiny")

print("Whisper model loaded")

def transcribe(audio_bytes: bytes) -> str:
    """
    Convert audio bytes to text using Whisper
    """
    print("Transcribing audio of size:", len(audio_bytes))

    # save temporary audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    print("Audio saved to temporary file:", tmp_path)
    result = model.transcribe(tmp_path, fp16=False)

    print("Transcription result:", result)

    os.remove(tmp_path)

    return result["text"]