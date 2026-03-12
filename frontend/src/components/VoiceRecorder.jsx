import { useState } from "react";

export default function VoiceRecorder() {

  const [recording, setRecording] = useState(false);
  const [result, setResult] = useState("");

  let mediaRecorder;
  let audioChunks = [];

  const startRecording = async () => {

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.start();

    setRecording(true);

    mediaRecorder.ondataavailable = event => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {

      const audioBlob = new Blob(audioChunks);

      sendAudio(audioBlob);

      audioChunks = [];
    };

    window.recorder = mediaRecorder;
  };

  const stopRecording = () => {
    window.recorder.stop();
    setRecording(false);
  };

  const sendAudio = async (audioBlob) => {

    const ws = new WebSocket("ws://localhost:8000/voice");

    ws.onopen = () => {
      audioBlob.arrayBuffer().then(buffer => {
        ws.send(buffer);
      });
    };

    ws.onmessage = async (event) => {

      const audioData = event.data;

      const audioBlob = new Blob([audioData]);

      const audioUrl = URL.createObjectURL(audioBlob);

      const audio = new Audio(audioUrl);
      audio.play();

      setResult("Agent processed your request successfully.");
    };
  };

  return (

    <div className="flex flex-col justify-center items-center">

      <button onClick={recording ? stopRecording : startRecording} className="border">

        {recording ? "Stop Recording" : "Start Recording"}

      </button>

      <h3 className="border w-fit">Agent Result</h3>

      <div>{result}</div>

    </div>
  );
}