from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
from pydantic import BaseModel
import os
import shutil
app = FastAPI(title="AI Chatbot Backend")

# Include chat routes
app.include_router(chat_router, prefix="/chat", tags=["Chat"])


app = FastAPI(title="AI Chatbot Backend")

# Add CORS middleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # Allow all origins; change to specific domains in production
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Include chat routes
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

# 📌 Store uploads in "uploads" folder
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---- Chat API ----
class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    # Echo-style bot for demo
    user_message = request.message
    bot_reply = f"🤖 Bot received: {user_message}"
    return {"response": bot_reply}

# ---- File Upload API ----
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save file to disk
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "filename": file.filename,
            "status": "success",
            "message": f"File '{file.filename}' uploaded successfully!"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}