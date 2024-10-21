# Importing libraries
import os
import requests as req
import time as t
import random as r
import sys as s


# Base variables and downloading files
directory_downloads = "C:/ChatBot-1.0.0/Downloads/Packages"
directory_conversation_logger = "C:/ChatBot-1.0.0/Conversations"
url = 'https://raw.githubusercontent.com/CommandBeat/chat-library/refs/heads/SCAI(Super-Cool-Artificial-Intelligence)/variable_safe.py'
"""
conversation_logger_folder = os.makedirs(directory_conversation_logger)
download_folder = os.makedirs(directory_downloads, exist_ok=True)
current_time = t.time()
if not os.path.exists(directory_conversation_logger):
    download_folder = os.makedirs(directory_conversation_logger, exist_ok=True)
random = r.randint(0, 100000000)
backup_random = r.randint(0, 100000000)
items = os.listdir(directory_conversation_logger)
"""

# renaming "-" to "_"/ hyphen to underscore
def rename_files(directory_conversation_logger):
    for filename in os.listdir(directory_conversation_logger):
            new_filename = filename.replace('-', '_')
            os.rename(os.path.join(directory_conversation_logger, filename), os.path.join(directory_conversation_logger, new_filename))
            print(f"Renamed: {filename} to {new_filename}")

# Commented base variables for no reason at all
"""
dir = "C:/Conversations"
current_time = t.time()
replies = {"...", "..", ".", ""}
database = {}
"""
random = r.randint(0, 100000000)
# backup_random = r.randint(0, 100000000)


# Scanning for any duplicates
def scan_directory(directory_conversation_logger):
    items = os.listdir(directory_conversation_logger)
    print(items)

def time(current_time):
    print(current_time)

# Asking starter question(for now the only one)
def ask():
    user_input = input("Hello! What do you want to chat about? ").lower()
    scan_directory(directory_conversation_logger)
    process(user_input, directory_conversation_logger)

# Processing text and saving it(into D:/Conversations/{file_name})
def process(user_input, directory_conversation_logger, database):
    summary = user_input
    data = summary
    file_name = summary + ".txt"
    folder = os.makedirs(directory_conversation_logger)
    backup_folder = folder # This isn't really needed, just in case
    path = os.path.join(directory_conversation_logger, file_name)
    with open(path, 'w') as file:
        file.write(data + random)
    reply(database)

# Saves it in database and tells the user
def reply(database):
    database = {{random}}
    print("Chat was successfully saved!")
    print(database)

reply(database)
