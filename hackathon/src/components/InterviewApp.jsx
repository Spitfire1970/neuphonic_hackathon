import { useState, useRef } from 'react';

const InterviewApp = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [status, setStatus] = useState('');
  const [error, setError] = useState('');
  const fileInputRef = useRef(null);
  const socketRef = useRef(null);

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file || !file.type.includes('pdf')) {
      setError('Please upload a PDF file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Upload failed');
      
      const data = await response.json();
      setStatus('PDF processed successfully. Ready to start interview.');
      setError('');
      
      // Connect to WebSocket after successful upload
      connectWebSocket();
    } catch (err) {
      setError('Error uploading file: ' + err.message);
    }
  };

  const connectWebSocket = () => {
    socketRef.current = new WebSocket('ws://localhost:8000/ws');
    
    socketRef.current.onopen = () => {
      setStatus('Connected to interview session');
    };

    socketRef.current.onmessage = (event) => {
      // Handle incoming audio data
      const audioBlob = new Blob([event.data], { type: 'audio/wav' });
      const audio = new Audio(URL.createObjectURL(audioBlob));
      audio.play();
    };

    socketRef.current.onerror = (error) => {
      setError('WebSocket error: ' + error.message);
    };
  };

  const startRecording = () => {
    if (!socketRef.current) {
      setError('Please upload a PDF first');
      return;
    }

    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);
        
        mediaRecorder.ondataavailable = (event) => {
          if (event.data.size > 0 && socketRef.current) {
            socketRef.current.send(event.data);
          }
        };

        mediaRecorder.start(100); // Send audio chunks every 100ms
        setIsRecording(true);
      })
      .catch(err => setError('Error accessing microphone: ' + err.message));
  };

  const stopRecording = () => {
    setIsRecording(false);
    // Stop all audio tracks
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        stream.getTracks().forEach(track => track.stop());
      });
  };

  return (
    <div className="container">
      <div className="card">
        <h1>AI Interview Assistant</h1>
        <div className="controls">
          <button 
            onClick={() => fileInputRef.current.click()}
            className="upload-btn"
          >
            Upload Interview PDF
          </button>
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileUpload}
            accept=".pdf"
            style={{ display: 'none' }}
          />
          
          <button 
            onClick={isRecording ? stopRecording : startRecording}
            className={`record-btn ${isRecording ? 'recording' : ''}`}
          >
            {isRecording ? 'Stop Recording' : 'Start Interview'}
          </button>

          {status && (
            <div className="status-message">
              {status}
            </div>
          )}
          
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}
        </div>
      </div>

      <style>{`
        .container {
          max-width: 800px;
          margin: 0 auto;
          padding: 20px;
        }

        .card {
          background: white;
          border-radius: 8px;
          padding: 24px;
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        h1 {
          text-align: center;
          margin-bottom: 24px;
          color: #333;
        }

        .controls {
          display: flex;
          flex-direction: column;
          gap: 16px;
        }

        button {
          padding: 12px 20px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 16px;
          transition: background-color 0.2s;
        }

        .upload-btn {
          background-color: #4f46e5;
          color: white;
        }

        .upload-btn:hover {
          background-color: #4338ca;
        }

        .record-btn {
          background-color: #22c55e;
          color: white;
        }

        .record-btn:hover {
          background-color: #16a34a;
        }

        .record-btn.recording {
          background-color: #ef4444;
        }

        .record-btn.recording:hover {
          background-color: #dc2626;
        }

        .status-message {
          padding: 12px;
          background-color: #f0fdf4;
          border: 1px solid #86efac;
          border-radius: 4px;
          color: #166534;
        }

        .error-message {
          padding: 12px;
          background-color: #fef2f2;
          border: 1px solid #fecaca;
          border-radius: 4px;
          color: #991b1b;
        }
      `}</style>
    </div>
  );
};

export default InterviewApp;