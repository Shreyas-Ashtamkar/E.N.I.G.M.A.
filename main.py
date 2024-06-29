from gui import init_chatbox, new_message, get_messages, show_message, ai_reply
import streamlit as st

st.title("E.N.I.G.M.A")
st.caption("Expert Network for Intelligent Guidance and Multi-task Assistance")

messages_container = st.container(border=True)
message_box = init_chatbox(height=550, container=messages_container)

with message_box:
    for i, msg in enumerate(get_messages()):
        if msg['role'] != 'system':
            show_message(msg['role'], msg['content'])

    if prompt := messages_container.chat_input(f"Type your message"):
        new_message(msg=prompt)
        ai_reply(container=message_box)

# from enigma import *

# MESSAGE_LIST = []

# app_response = process(MESSAGE_LIST)

# print(app_response)
