from services.speech_to_text.whisper_stt import transcribe


def speech_to_text(audio_bytes):

    if len(audio_bytes) < 10000:
        return ""

    return transcribe(audio_bytes)