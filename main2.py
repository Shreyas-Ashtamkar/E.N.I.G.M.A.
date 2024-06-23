import ollama, json

SYSTEM_PROMPT = """
You are a helpful assistant, with internal ability of function calling. 
The end user does not understand directly the functions so he may not give precise details. 
Ask the user the missing details in a conversation and then return a function call or respond with appropriate message.
You are to either return a function call, or respond normally, as whatever is required.
Answer in short and straightforward way.

Only if required, to call the function, return with a JSON format - 
{
    "tool" : "tool_name",
    "tool_kwargs": {
        "arg1" : "val1",
        "arg2 : "val2"
    }
}
otherwise respond by talking about the topic requested by user.

The functions/tools provided to you with their arguments/parameters and descriptions are as follows. 
    1.  get_current_weather
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state/country, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": [
                            "celsius",
                            "fahrenheit"
                        ]
                    },
                },
                "required": [
                    "location"
                ]
            }
        }
    2.  get_current_time
        {
            "name": "get_current_time",
            "description": "Get the local time at the pricise location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city from where the local time is needed of.",
                    },
                    "country": {
                        "type": "string",
                        "description": "The country of the city from where local time is needed.",
                    },
                },
                "required": [
                    "city"
                ]
            }
        }
"""

message_list=[
    {
        'role'    : 'system',
        'content' : SYSTEM_PROMPT,
    },
    {
        'role'    : 'user',
        'content' : "What's the weather in Africa?"
    },
    {
        'role'    : 'assistant',
        'content' : "To get the current weather in a specific location, I'd need more information. Could you please provide the city and country in Africa where you're interested in knowing the time? It could be anywhere from Cape Town to Cairo!"
    },
    {
        'role'    : 'user',
        'content' : "Maybe, I don't know, Cairo?"
    },
]

model_list = [
    # 'phi3',
    'mistral',
    'llama3',
    # 'gemma'
]


for m in model_list:
    assistant = ollama.chat(
        model    = m,
        messages = message_list
    )
    response = assistant['message']['content']
    print(f"----------{m}-----------")
    try:
        response_function = json.loads(response)
        print("Function Called :", response_function)
    except Exception as e:
        print("Function not called")
        print(response)
        
