import google.generativeai as genai
from decouple import config
from .test import to_markdown

API_KEY = config("GOOGLE_API_KEY", default="AIzaSyCnMz4nOPyugJHhQu3qB8eydCzje8EDzzQ")
genai.configure(api_key=API_KEY)



def geminiChat():
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content("What is the meaning of life?")
    #print(response.text)

# class Conversation():

#     def __init__(self, history):
#         history = history

    
    #             {
    #                 "role": "user",
    #                 "parts": ["Hello, I have 2 dogs in my house."],
    #             },
    #             {
    #                 "role": "model",
    #                 "parts": ["Great to meet you. What would you like to know?"],
    #             },
    #             ] )

def geminiConversation(problem:str, history:list):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=history)
    response = chat.send_message(f"You an AI research assitant named Cimplify and you would help people with their research and questions by proividing very detailed and professional answers to their questions below. \n\n \
                                Question: {problem}")
    conversation = []
    for message in chat.history:
        conversation.append({message.role: message.parts[0].text})
    print(chat.history)
    return {"Response": to_markdown(response.text), "Chat_History": conversation}


# conv = ""
# while conv != "Stop":
#     conv = geminiConversation(str(input("User: ")), history= [{
#                                                                 "role": "user",
#                                                                 "parts": ["Hello, I have 2 dogs in my house."],
#                                                             },
#                                                             {
#                                                                 "role": "model",
#                                                                 "parts": ["Great to meet you. What would you like to know?"],
#                                                                                                                                     }])
