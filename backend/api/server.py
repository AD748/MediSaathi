from fastapi import FastAPI
from backend.api.voice_socket import voice_stream
from fastapi import WebSocket

app = FastAPI(
    title="Voice AI Clinical Agent",
    description="Real-time multilingual voice AI for appointment booking",
    version="1.0"
)

@app.get("/")
def health_check():
    return {"status": "Voice AI Agent Running"}

@app.websocket("/voice")
async def websocket_endpoint(websocket: WebSocket):
    await voice_stream(websocket)