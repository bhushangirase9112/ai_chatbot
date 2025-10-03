from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router
from pydantic import BaseModel
from fastapi.responses import JSONResponse
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

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        return {"status": "success", "filename": file.filename, "path": file_path}
    except Exception as e:
        return JSONResponse(content={"status": "error", "detail": str(e)}, status_code=500)