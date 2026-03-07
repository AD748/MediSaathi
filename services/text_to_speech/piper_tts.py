import subprocess
import uuid


PIPER_PATH = r"C:\piper\piper.exe"
MODEL_PATH = r"C:\piper\models\en_US-lessac-medium.onnx"


def synthesize(text):

    output_file = f"tts_{uuid.uuid4()}.wav"

    command = [
        PIPER_PATH,
        "--model",
        MODEL_PATH,
        "--output_file",
        output_file
    ]

    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    process.communicate(text)

    with open(output_file, "rb") as f:
        audio_bytes = f.read()

    return audio_bytes