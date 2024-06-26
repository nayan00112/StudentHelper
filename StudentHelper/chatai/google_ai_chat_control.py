import google.generativeai as genai
from decouple import config

# https://ai.google.dev/gemini-api/docs/api-key?authuser=1
GOOGLE_API_KEY = config("chatapi")

genai.configure(api_key=GOOGLE_API_KEY)

def sayhello():
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    return chat 

def askme(chat, que):
    response = chat.send_message(que)
    return response.text