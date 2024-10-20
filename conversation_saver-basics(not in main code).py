import os

user_input = input("Hello! What seems to be the problem? ")
file_name = user_input + ".txt"
dest = "D:/Conversations"
folder = os.makedirs(dest, exist_ok=True)
path = os.path.join(dest, file_name)
with open(path, 'w') as file:
    file.write(user_input + ".")
