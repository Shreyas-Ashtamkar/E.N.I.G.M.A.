from enigma import *

MESSAGE_LIST = [
    {
        "role": "user",
        "content": "What's the time in New York right now?"
    },
]

app_response = process(MESSAGE_LIST)

print(app_response)
