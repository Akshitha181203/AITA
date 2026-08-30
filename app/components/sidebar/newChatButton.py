import streamlit as st


def render_new_chat_button():

    if st.button("+ New Chat"):

        new_chat_id = (
            f"Chat {len(st.session_state.chat_sessions) + 1}"
        )

        st.session_state.chat_sessions[new_chat_id] = []

        st.session_state.current_chat_id = new_chat_id

        st.session_state.messages = []

        st.session_state.current_screen = "chat"