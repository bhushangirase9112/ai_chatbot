from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Request schema
class ChatRequest(BaseModel):
    message: str

# Response schema
class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chatbot endpoint
    Example:
    Input:  {"message": "Hello"}
    Output: {"response": "Hi there! How can I help you today?"}
    """
    
    user_message = request.message.lower()

    # Simple rule-based responses (can later plug in AI model)
    if "hello" in user_message or "hi" in user_message:
        bot_reply = "Hi there! 👋 How can I help you today?"
    elif "bye" in user_message:
        bot_reply = "Goodbye! Have a great day!"
    elif "help" in user_message:
        bot_reply = "Sure! You can ask me any question and I'll try to assist."
    else:
        bot_reply = "I'm just a simple chatbot 🤖. Try saying 'hello' or 'help'."

    return ChatResponse(response=bot_reply)
