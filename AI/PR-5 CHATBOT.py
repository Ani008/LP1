# Develop an elementary chatbot for any suitable customer interaction application.

import random

responses = {
    "greeting": ["Hello!", "Hi!"],
    "farewell": ["Goodbye!", "Take care!"],
    "thanks": ["You're welcome!", "Glad to help!"],
    "default": ["Sorry, I didn't understand."]
}

def generate_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "bye" in user_input:
        return random.choice(responses["farewell"])
    elif "thank" in user_input:
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

def chatbot():
    print("Chatbot: Hi! How can I assist you?")
    while True:
        user_input = input("You: ")
        response = generate_response(user_input)
        print("Chatbot:", response)
        if "bye" in response:
            break

chatbot()