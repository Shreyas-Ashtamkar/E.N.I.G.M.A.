import json
import enigma
from utils.gui import restart_chat, st, init_chatbox, new_message, get_messages, show_message, ai_reply

st.set_page_config(initial_sidebar_state="collapsed")

st.title("E.N.I.G.M.A")
st.caption("Expert Network for Intelligent Guidance and Multi-task Assistance")

messages_container = st.container(border=True)
message_box = init_chatbox(height=550, container=messages_container)

with st.sidebar:
    st.header("Conversation Actions")
    st.button("Restart", on_click=restart_chat, use_container_width=True, type="primary")
    st.download_button("Download", json.dumps(get_messages()), use_container_width=True, type="secondary")

with message_box:
    for i, msg in enumerate(get_messages()):
        if msg['role'] != 'system':
            show_message(msg['role'], msg['content'])

    if prompt := messages_container.chat_input(f"Type your message"):
        new_message(msg=prompt)
        ai_reply(container=message_box, ai=enigma.process)
    