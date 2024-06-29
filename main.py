from utils import *

MESSAGE_LIST = [
    {
        'role'    : 'user',
        'content' : "Book an uber cab for me to go home."
    },
]

chat_response = process(MESSAGE_LIST)

print(chat_response)
