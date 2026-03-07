from fastapi import WebSocket
from backend.controllers.voice_pipeline import process_voice


async def voice_stream(websocket: WebSocket):

    await websocket.accept()

    audio_buffer = b""

    while True:

        audio_chunk = await websocket.receive_bytes()
        audio_buffer += audio_chunk
        # if audio_chunk == b"INTERRUPT":
        #     audio_buffer = b""


        # process after certain buffer size
        if len(audio_buffer):

            response_audio = await process_voice(audio_buffer)

            await websocket.send_bytes(response_audio)

            audio_buffer = b""