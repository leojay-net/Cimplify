import google.generativeai as genai


API_KEY = "AIzaSyCnMz4nOPyugJHhQu3qB8eydCzje8EDzzQ"
genai.configure(api_key=API_KEY)



def geminiChat():
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content("What is the meaning of life?")
    #print(response.text)



model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def geminiConversation(problem):
    response = chat.send_message(f"You an AI research assitant named Cimplify and you would help people with their research and questions by proividing very detailed and professional answers to their questions below. The conversation might probably start with a greeting so reply with using this format: \n\n \
                                 Question: {problem}")
    print("Model:",response.text)
    conversation = []
    for message in chat.history:
        conversation.append({message.role: message.parts[0].text})
    return {"Response": response.text, "Chat_History": conversation}


# conv = ""
# while conv != "Stop":
#     conv = geminiConversation(str(input("User: ")))