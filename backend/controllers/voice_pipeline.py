import time

from sqlalchemy import text

from services.speech_to_text.stt_service import speech_to_text
from services.language_detection.detector import detect_language
from agent.reasoning.agent_core import interpret
from agent.tools.booking_tool import book_tool
from backend.controllers.latency_logger import log_latency
from agent.reasoning.llm_agent import extract_intent
from agent.tools.tool_router import execute_tool
from memory.session_memory.redis_memory import save_session, get_session
from services.text_to_speech.tts_service import text_to_speech


async def process_voice(audio_bytes):

    start_time = time.time()

    # Step 1 — Speech to Text
    print("Received audio size:", len(audio_bytes))
    text = speech_to_text(audio_bytes)
    print("STT result:", text)

    if not text.strip():
        return b""

    stt_time = time.time()

    # Step 2 — Language Detection
    language = detect_language(text)

    lang_time = time.time()
    # Step 3 — Agent Reasoning

    intent_data = extract_intent(text)
    tool_result = execute_tool(intent_data)
    response_text = str(tool_result)
    print("Intent:", intent_data)

    session_id= "patient_1"
    session_data = get_session(session_id)
    session_data.update(intent_data)

    save_session(session_id, session_data)

    tool_time = time.time()

    # Step 5 — Text to Speech
    audio_response = text_to_speech(response_text)

    print("Response text:", response_text)

    tts_time = time.time()

    latency = (tts_time - start_time) * 1000

    metrics = {
        "stt_latency_ms": (stt_time - start_time) * 1000,
        "language_latency_ms": (lang_time - stt_time) * 1000,
        "agent_latency_ms": latency,
        "tool_latency_ms": (tool_time - lang_time) * 1000,
        "tts_latency_ms": (tts_time - tool_time) * 1000,
        "total_latency_ms": latency
    }

    print("Latency metrics:", metrics)

    log_latency(metrics)
    
    print("Transcribed text:", text)

    return audio_response