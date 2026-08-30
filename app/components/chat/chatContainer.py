import streamlit as st


def render_chat_container():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])