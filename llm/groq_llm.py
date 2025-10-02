from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq( api_key=GROQ_API_KEY)


def groq_llm(user_query):
    bot_reply = ""
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[
        {
            "role": "user",
            "content": user_query
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )
    for chunk in completion:
        content = chunk.choices[0].delta.content 
        if content:
            bot_reply += content
    
    return bot_reply