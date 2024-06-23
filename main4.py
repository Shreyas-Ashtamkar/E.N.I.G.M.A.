import ollama
from system_prompt import SYSTEM_PROMPT

SELECTED_AI = "mistral"

# MESSAGES_LIST = [
#     {
#         'role'    : 'system',
#         'content' : SYSTEM_PROMPT[SELECTED_AI],
#     },
#     {
#         'role'    : 'user',
#         'content' : "Can you Create a text file with numbers written from 1 to 6000 ?"
#     },
#     {
#         'role'    : 'assistant',
#         'content' : "I'd be happy to help! Can you please tell me what kind of file you would like me to create? Would it be a text file, image file, document, or something else? Additionally, do you have any specific name in mind for the file?"
#     },
#     {
#         'role'    : 'user',
#         'content' : 'Just a normal text file, with a poem about apples. ?'
#     }
# ]

MESSAGES_LIST = [
    { 
        'role'    : 'system',
        'content' : SYSTEM_PROMPT[SELECTED_AI],
    },
    # {
    #     'role'    : 'user',
    #     'content' : "Hey can you help me research about Laptops and their origin?"
    # },
    # {
    #     'role'    : 'assistant',
    #     'content' : "Certainly! Early laptops began with IBM Portable PC, evolved through models like Kaypro II, leading to modern laptops featuring Intel processors, USB connectivity, touchpads, and advanced graphics. Brands such as Apple (MacBook series) and Dell have significantly impacted the laptop market."
    # },
    {
        'role'    : 'user',
        'content' : "K."
    }
]

# client = ollama.Client()

assistant_response = ollama.chat(
    model    = SELECTED_AI,
    messages = MESSAGES_LIST
)['message']['content'].strip()

print(assistant_response)
