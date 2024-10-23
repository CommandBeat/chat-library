# Importing libraries
import os
import random as r
import time as t
import nltk
from nltk.chat.util import Chat, reflections
import re


# Base variables(for now)
current_time = t.time() # No need for this
id = 0
databse = {}
directory_downloads = "C:/ChatBot-1.0.0/Downloads/Packages"
directory_conversation_logger = "C:/ChatBot-1.0.0/Conversations"
pairs = [ # Main variable
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["My name is SCAI(Super Cool Artificial Intelligence)",]
    ],
    [
        r"how are you?",
        ["I'm doing great, thanks for asking!",]
    ],
    [
        r"sorry (.*)" or r"sorry, (.*)",
        ["No problem at all.",]
    ],
    [
        r"I (.*) (good|well|okay|ok|fine)",
        ["Glad to hear that your %1!",]
    ],
    [
        r"quit" or r"exit chat" or r"quit chat" or r"bye" or r"bye bye" or r"bye-bye" or r"i have to leave" or r"i have to go" or r"bye, (.*)" or r"bye-bye, (.*)" or r"bye bye, (.*)" or r"bye (.*)" or r"bye-bye (.*)" or r"bye bye (.*)" or r"i am leaving" or r"..." or r".." or r"." or r" ",
        ["Bye! Take care.",]
    ],
]


# Base function
def chat(pairs):
    chatbot = Chat(pairs, reflections)
    print("Hi, I'm your chatbot, SCAI! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        match = re.match(pairs[5][0], user_input, re.IGNORECASE)
        if match:
            print("SCAI: ", pairs[5][1])
    response = chatbot.respond(user_input)
    print("SCAI: ", response)

# Using the function
chat(pairs)
