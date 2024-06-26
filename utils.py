import json
from aitools import _AI, _Request, SimpleNamespace
from system_prompt import SYSTEM_PROMPT

DEBUG   = True
VERBOSE = 10
dummy_print = lambda x, *y, **z: ""
print = print if DEBUG else dummy_print
print2 = print if VERBOSE > 1 else dummy_print
print3 = print if VERBOSE > 2 else dummy_print
print4 = print if VERBOSE > 3 else dummy_print


AI = SimpleNamespace(
    conversation = _AI(
        model  = "llama3",
        prompt = SYSTEM_PROMPT["CONVERSATION"],
        default_response = "Hey sorry can you elaborate a bit more?"
    ),
    summary = _AI(
        model  = "phi3",
        prompt = SYSTEM_PROMPT["SUMMARY"],
        default_response = "NO_SUMMARY",
        response_tester = lambda resp: ("Do this -" in resp)
    ),
    function = _AI(
        model  = "mistral",
        prompt = SYSTEM_PROMPT["FUNCTION"],
        default_response = """{"tool":"conversation"}""",
        default_error    = """{"tool":"error", "tool_kwargs":"I don't have the ability to do that yet."}""",
        response_tester  = lambda resp: resp[0] == "{" and resp[-1] == "}"
    )
)


def _stringify_conversation(conversation):
    string_conversation = ""
    for message in conversation:
        role, content = message['role'], message['content']
        if role == "system": continue
        string_conversation += f"\n{role}:{content}\n"
    
    print3("\n_stringify_conversation :", string_conversation)
    return string_conversation.strip()


def _get_summary(conversation:list[dict[str,str]]=None) -> str:
    conversation = _stringify_conversation(conversation)
    summary:str = AI.summary.simple_chat(conversation)
    return summary.strip()


def get_request_type(conversation:str) -> _Request:
    summary = _get_summary(conversation)
    request_type = "CONVERSATION"
    request_data = ""
    if "Do this - " in summary:
        request_type = "FUNCTION"
        request_data = summary.split("\n")[0][10:]
    return _Request(type_=request_type, data_=request_data)
        

def get_function(task):
    function_details = AI.function.default_response
    try:
        function_details:dict = json.loads(AI.function.simple_chat(task))
    except Exception as e:
        print(e)
    print("function_details :", function_details)
    return function_details


def continue_conversation(conversation:list[dict[str:str]]):
    return AI.conversation.chat(conversation)


def process(conversation):
    summary = _get_summary(conversation)
    # _get_request_type
    if "NO_SUMMARY" in summary:
        print(" -- Conversation -- ")
        message = continue_conversation(conversation)
        print("message :", message)
    else:
        print(" -- Function -- ")
        task = summary.split("\n")[0][10:]
        print("task :", task)
        function_details = get_function(task)
        if function_details['tool'] == 'conversation':
            message = continue_conversation(conversation)
            print("message :", message)
        elif function_details['tool'] == 'error':
            conversation.append({
                'role' : 'system',
                'message': function_details['tool_kwargs'].get("message")
            })
            message = continue_conversation(conversation)
            print("message :", message)
        message = continue_conversation(conversation)
        print("message :", message)


if __name__ == "__main__":
    process()
