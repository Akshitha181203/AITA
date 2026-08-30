import streamlit as st


def render_chat_rooms():

    st.subheader("Chats")

    for chat_id in st.session_state.chat_sessions.keys():

        if st.button(chat_id):

            st.session_state.current_chat_id = chat_id
            st.session_state.current_screen = "chat"

            st.session_state.messages = (
                st.session_state.chat_sessions[chat_id]
            )