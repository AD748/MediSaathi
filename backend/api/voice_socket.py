from fastapi import WebSocket
from backend.controllers.voice_pipeline import process_voice
from services.vad.vad_service import detect_speech
from services.vad.audio_utils import bytes_to_tensor


async def voice_stream(websocket: WebSocket):

    await websocket.accept()

    audio_buffer = b""

    while True:

        audio_chunk = await websocket.receive_bytes()
        audio_buffer += audio_chunk
        audio_tensor = bytes_to_tensor(audio_buffer)

        if detect_speech(audio_tensor):
            continue
        # if audio_chunk == b"INTERRUPT":
        #     audio_buffer = b""


        # process after certain buffer size
        # if len(audio_buffer):

        response_audio = await process_voice(audio_buffer)

        await websocket.send_bytes(response_audio)

        audio_buffer = b""