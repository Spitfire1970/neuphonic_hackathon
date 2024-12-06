from fastapi import FastAPI, UploadFile, WebSocket, File
from fastapi.middleware.cors import CORSMiddleware
import pypdf
import os
import asyncio
from pyneuphonic import Neuphonic, Agent, AgentConfig
import tempfile
import io
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables to store the current agent and context
current_agent = None
interview_context = None

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global current_agent, interview_context
    
    if not file.filename.endswith('.pdf'):
        return {"error": "File must be a PDF"}
    
    try:
        # Read the PDF content
        content = await file.read()
        pdf_file = io.BytesIO(content)
        pdf_reader = pypdf.PdfReader(pdf_file)
        
        # Extract text from all pages
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Store the context
        interview_context = text

        # Create a prompt using the extracted text
        prompt = f"""You are an AI interviewer. Use the following context for the interview:
        {text}
        
        Conduct the interview in a professional manner, asking relevant questions based on the provided context.
        Wait for the candidate's response before asking the next question."""

        # Initialize Neuphonic agent
        try:
            client = Neuphonic(api_key="fd670d8dde423652a2b03922b9c3178a781191c6e5c51a3a5501ffbba752d2db.b572ca47-5ec5-461b-82a0-e28fefeed32f")
            agent_response = client.agents.create(
                name='Interviewer',
                prompt=prompt,
                greeting='Hello, I will be conducting your interview today. Are you ready to begin?'
            )
            
            agent_id = agent_response['data']['id']
            logger.info(f"Created agent with ID: {agent_id}")
            
            # Create and store the agent
            current_agent = Agent(client, agent_id=agent_id, tts_model='neu_hq')
            
            return {"success": True, "agent_id": agent_id, "context_length": len(text)}
        
        except Exception as e:
            logger.error(f"Error creating agent: {str(e)}")
            return {"error": f"Failed to create agent: {str(e)}"}
    
    except Exception as e:
        logger.error(f"Error processing PDF: {str(e)}")
        return {"error": str(e)}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global current_agent
    
    try:
        await websocket.accept()
        logger.info("WebSocket connection accepted")
        
        if not current_agent:
            await websocket.send_text("No agent available. Please upload a PDF first.")
            await websocket.close()
            return
        
        # Start the agent
        await current_agent.start()
        logger.info("Agent started successfully")
        
        while True:
            try:
                # Receive audio data from client
                audio_data = await websocket.receive_bytes()
                logger.info("Received audio data")
                
                # Process audio with Neuphonic agent
                response = await current_agent.process_audio(audio_data)
                logger.info("Processed audio data")
                
                # Send audio response back to client
                await websocket.send_bytes(response)
                logger.info("Sent response")
                
            except Exception as e:
                logger.error(f"Error processing audio: {str(e)}")
                break
            
    except Exception as e:
        logger.error(f"WebSocket error: {str(e)}")
    finally:
        if websocket.client_state.CONNECTED:
            await websocket.close()
        logger.info("WebSocket connection closed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)