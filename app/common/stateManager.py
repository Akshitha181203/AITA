import streamlit as st


def initialize_session_state():

    defaults = {
        "current_screen": "chat",
        "selected_version": "v1.0 Basic Chat",
        "messages": [],
        "chat_sessions": {
            "Chat 1": []
        },
        "current_chat_id": "Chat 1",
        "uploaded_pdf_text": ""
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value