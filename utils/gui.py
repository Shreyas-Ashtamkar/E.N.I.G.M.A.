from types import FunctionType
import streamlit as st

def _ai(request:str):
    reply = "No AI set"
    return reply

async def _ai_stream(request:str):
    reply = "No AI set"
    for chunk in reply:
        content = chunk
        yield content


def init_chat():
    print("Called init_chat")
    st.session_state["chat_history"] = [{
        'role': "assistant",
        # 'content': ollama_fetch_response(model="phi3", stream=False),
        'content': f"Hello I am Enigma. How may I help you?.",
    }]
    
    return st.session_state["chat_history"]


def get_messages():
    if "chat_history" not in st.session_state:
        init_chat()
    return st.session_state["chat_history"]


def init_chatbox(height=550, container=st):
    return container.container(height=height, border=True)


def show_message(role='user', msg='This is new message', container=st):
    return container.chat_message(role).write(msg)


def new_message(role: str = "user", msg: str = "This is new message", container=st):
    st.session_state["chat_history"].append({'role': role, 'content': msg})
    return show_message(role, msg, container)


def ai_stream_response(ai:FunctionType = None):
    if not ai:
        ai = _ai_stream
    reply = ai(get_messages())
    
    for chunk in reply:
        content = chunk
        yield content
    
def ai_fetch_response(ai:FunctionType = None):
    if not ai:
        ai = _ai
    reply = ai(get_messages())
    return reply


def ai_reply(container=st, stream=False, ai=None):
    if stream:
        response = ai_stream_response(ai=ai)
        container.chat_message('assistant').write_stream(response)
    else:
        response = ai_fetch_response(ai=ai)
        # print("printing response :", response)
        container.chat_message('assistant').write(response)

    st.session_state["chat_history"].append({'role': 'assistant', 'content': response})
