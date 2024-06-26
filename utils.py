from aitools import AI
import json

def _stringify_conversation(conversation):
    string_conversation = ""
    for message in conversation:
        role, content = message['role'], message['content']
        if role == "system": continue
        string_conversation += f"\n{role}:{content}\n"
    return string_conversation.strip()

def get_summary(conversation:list[dict[str,str]]=None) -> str:
    conversation = _stringify_conversation(conversation)
    summary = AI.summary.simple_chat(conversation)
    return summary.strip()

def get_request_type(summary:str) -> str:
    pass

def get_function_call():
    pass

def continue_conversation(conversation:list[dict[str:str]]):
    return AI.conversation.chat(conversation)


def process(conversation):
    summary = get_summary(conversation)
    if "NO_SUMMARY" in summary:
        print(" -- Conversation -- ")
        message = continue_conversation(conversation)
        print("message :", message)
    else:
        print(" -- Function -- ")
        task = summary.split("\n")[0][10:]
        print("task :", task)
        function_details = AI.function.simple_chat(task)
        print("function_details :", function_details)
        try:
            function_details:dict = json.loads(function_details)
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
        except Exception as e:
            print("--------------------",e)
            message = continue_conversation(conversation)
            print("message :", message)

if __name__ == "__main__":
    process()
