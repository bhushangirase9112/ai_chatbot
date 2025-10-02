from llm.groq_llm import groq_llm

def chat(user_query):
    try:
        bot_reply = groq_llm(user_query)
    except Exception as e:
        return e
    return bot_reply