import streamlit as st
from enigma import process


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


def ai_stream_response():
    reply = process(
        get_messages(),
        stream=True
    )
    
    for chunk in reply:
        content = chunk
        yield content
    
def ai_fetch_response():
    reply = process(
        get_messages()
    )
    
    return reply


def ai_reply(container=st, stream=False):
    if stream:
        response = ai_stream_response()
        message = container.chat_message('assistant').write_stream(response)
    else:
        response = ai_fetch_response()
        print("printing response :", response)
        message = container.chat_message('assistant').write(response)

    st.session_state["chat_history"].append({'role': 'assistant', 'content': response})
