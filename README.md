# 🤖 AI Chatbot Backend (FastAPI)

This is a simple **AI Chatbot backend** built using **FastAPI**.  
It provides a single API endpoint to send a user query and receive a chatbot response.  
The Flutter frontend will consume this API.

---

## 🚀 Features
- Built with **FastAPI**
- One endpoint: `/chat`
- Accepts a user query and returns chatbot response
- Lightweight and easy to extend

---

## 🛠️ Setup Instructions

### 1. Clone the repository

    git clone https://github.com/your-username/ai-chatbot-backend.git
    cd ai-chatbot-backend


### 1. Create & activate virtual environment
    ### Create venv
    python -m venv venv

    # Activate (Linux/Mac)
    source venv/bin/activate

    # Activate (Windows)
    venv\Scripts\activate



### 3. Install dependencies
    pip install -r requirements.txt


### 4. Run the Server
    ###Use Uvicorn to start the FastAPI server:
    uvicorn main:app --reload
