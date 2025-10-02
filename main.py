from fastapi import FastAPI
from api.chat import router as chat_router

app = FastAPI(title="AI Chatbot Backend")

# Include chat routes
app.include_router(chat_router, prefix="/chat", tags=["Chat"])
