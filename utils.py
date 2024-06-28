import json
from aitools import _AI, _Request, _format_message
from toolutils import Tool

from app_configs import *

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
    summary:str = AI.summary.simple_chat(conversation).strip()
    print2("\n----------_get_summary called----------")
    print3(summary)
    return summary


def _get_request(summary:str) -> _Request:
    request = _Request(type_="CONVERSATION", data_="")
    if "Do this - " in summary:
        request.type_ = "FUNCTION"
        request.data_ = summary.split("\n")[0][10:]
    print2("\n------------_get_request called-------------")
    print2(f"Type:{request.type_} \nData:'{request.data_}'")
    return request
        

def _get_tool(task:str):
    tool_details = AI.tool.default_response
    try:
        tool_details:dict = json.loads(AI.tool.simple_chat(task))
    except Exception as e:
        print(e)
    print2("\n------------_get_tool called-------------")
    print3(tool_details)
    return tool_details


def _run_tool(tool_details:dict, retry=0):
    tool_name:Tool   = tool_details.get('tool')
    tool_kwargs:dict = tool_details.get('tool_kwargs')
    try:
        tool = Tool.get(tool_name)
        print2("\n------------_run_tool called-------------")
        tool_response = tool.exec(**tool_kwargs)
    except Exception as e:
        if retry < MAX_RETRY:
            tool_response = _run_tool(tool_details, retry+1)
        tool_response = hint_error(error_message=e.__str__())
    return tool_response

    
def _continue_conversation(conversation:list[dict[str:str]]):
    print2("\n------------_continue_conversation called-------------")
    print(conversation)
    return AI.conversation.chat(conversation)


# def process(conversation):
#     summary = _get_summary(conversation)
#     if "NO_SUMMARY" in summary:
#         message = continue_conversation(conversation)
#         print("message :", message)
#     else:
#         task = summary.split("\n")[0][10:]
#         print("task :", task)
        
#         tool_details = _get_tool(task)
#         if tool_details['tool'] == 'conversation':
#             pass
#         elif tool_details['tool'] == 'error':
#             conversation.append({
#                 'role' : 'system',
#                 'content': tool_details['tool_kwargs'].get("message")
#             })
#         else:
#             conversation.append({
#                 'role' : 'system',
#                 'content' : f'Called tool - {tool_details["tool"]}'
#             })

#         print("message :", message)
#         message = continue_conversation(conversation)


def process(conversation:list[dict[str:str]]):
    summary = _get_summary(conversation)
    
    request = _get_request(summary)
    
    if request.type_ == "FUNCTION":
        # Run the tool
        tool_details  = _get_tool(request.data_)
        tool_response = _run_tool(tool_details)
        
        conversation.append(_format_message("Inform the user - "+tool_response, role='system'))
    
    # Continue Conversation
    print("\nContinue Conversation")
    chat_response = _continue_conversation(conversation)
    print(chat_response)
    
    


if __name__ == "__main__":
    process([
        {
            'role' : 'user',
            'content':"Hey GPT! What's up?"
        },
        {
            'role' : 'assistant',
            'content':"Hello, Shreyas! I'm here and ready to help. How can I assist you today?"
        },
        {
            'role' : 'user',
            'content':"I'm trying to check how the weather will be today in the evening in Pune. Can you help?"
        }
    ])
