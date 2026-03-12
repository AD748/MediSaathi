import { useState } from "react";

export default function VoiceAssistant() {

  const [recording, setRecording] = useState(false);
  const [messages, setMessages] = useState([]);

  let mediaRecorder;
  let chunks = [];

  const startRecording = async () => {

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.start();

    setRecording(true);

    mediaRecorder.ondataavailable = e => {
      chunks.push(e.data);
    };

    mediaRecorder.onstop = () => {

      const audioBlob = new Blob(chunks);

      sendAudio(audioBlob);

      chunks = [];
    };

    window.recorder = mediaRecorder;
  };

  const stopRecording = () => {
    window.recorder.stop();
    setRecording(false);
  };

  const sendAudio = (blob) => {

    const ws = new WebSocket("ws://localhost:8000/voice");

    ws.onopen = async () => {

      const buffer = await blob.arrayBuffer();

      ws.send(buffer);

      setMessages(prev => [
        ...prev,
        { role: "user", text: "Voice input sent..." }
      ]);
    };

    ws.onmessage = async (event) => {

      const audioBlob = new Blob([event.data]);

      const url = URL.createObjectURL(audioBlob);

      const audio = new Audio(url);

      audio.play();

      setMessages(prev => [
        ...prev,
        { role: "agent", text: "Agent processed request" }
      ]);
    };
  };

  return (

    <div className="max-w-2xl mx-auto p-6">

      <h1 className="text-3xl font-bold text-center mb-6">
        Voice AI Assistant
      </h1>

      {/* Status */}

      <div className="flex justify-center mb-6">

        <div className={`px-4 py-2 rounded-full text-white
          ${recording ? "bg-red-500" : "bg-green-500"}
        `}>

          {recording ? "Recording..." : "Idle"}

        </div>

      </div>

      {/* Record Button */}

      <div className="flex justify-center mb-8">

        <button
          onClick={recording ? stopRecording : startRecording}
          className={`w-20 h-20 rounded-full text-white text-xl
          ${recording ? "bg-red-500" : "bg-blue-600"}
          hover:scale-105 transition`}
        >

          🎙

        </button>

      </div>

      {/* Conversation */}

      <div className="bg-gray-100 rounded-xl p-4 h-96 overflow-y-auto">

        {messages.map((m, i) => (

          <div
            key={i}
            className={`mb-3 p-3 rounded-lg
            ${m.role === "user"
              ? "bg-blue-200 text-right"
              : "bg-white"}
            `}
          >

            {m.text}

          </div>

        ))}

      </div>

    </div>

  );
}