from fastapi import APIRouter
from groq import Groq
from schemas.chat_schema import ChatRequest, ChatResponse
from services.chat_service import chat

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chatbot endpoint
    Example:
    Input:  {"message": "Hello"}
    Output: {"response": "Hi there! How can I help you today?"}
    """
    
    user_message = request.message.lower()
    response = chat(user_message)

    return ChatResponse(response=response)
