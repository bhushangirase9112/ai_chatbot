from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.chat import router as chat_router

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
