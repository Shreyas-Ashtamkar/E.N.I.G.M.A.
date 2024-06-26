import ollama
from system_prompt import SYSTEM_PROMPT

SELECTED_AI = "dolphin-llama3"

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
        'content' : "Send an email summarizing the discussion about learning Node.js and Python."
    },
]

# MESSAGES_LIST = messages = [
#     { 
#         'role'    : 'system',
#         'content' : SYSTEM_PROMPT[SELECTED_AI],
#     },
#     {
#         "role": "user",
#         "content": """user: Hey! How do you do?

# assistant: I'm doing well, thanks for asking! I'm just an AI, so I don't have feelings or emotions like humans do, but I'm always happy to chat and help with any questions or topics you'd like to discuss. What's on your mind today?

# user: I'm just having a really good day, programming and eating a cheeze burgar.

# assistant: That sounds like an amazing combination! Programming can be so satisfying when things go well, and adding a delicious cheeseburger to the mix is the perfect way to cap off a great day. What have you been working on in your programming endeavors? Any exciting projects or new skills you're learning?

# user: I'm just learning Node.js and Python, but seems like even though there's a lot of common, both are not used together much often.

# assistant: Node.js and Python are both popular and powerful programming languages, but they do have different use cases and philosophies. ...

# user: Okay! That was really informative. Tell me. Is there something I can do to help you out?

# assistant: Thank you for your offer! While I don't require assistance in the traditional sense, it's always great to know that my input is appreciated. If you have any programming questions or need guidance on Node.js and Python usage, feel free to ask and I'll be more than happy to help out with information and insights.

# user: Now can you sent me an email with the summary of what we discussed?""",
#     },
    
# ]

# client = ollama.Client()

assistant_response = ollama.chat(
    model    = SELECTED_AI,
    messages = MESSAGES_LIST
)['message']['content'].strip()

print(assistant_response)
