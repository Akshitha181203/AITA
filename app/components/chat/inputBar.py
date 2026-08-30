import streamlit as st

from app.components.pdf.pdfUploadButton import render_pdf_upload
from app.versions.v1_basicChat import run_v1_basic_chat
from app.versions.v1_contextInjection import run_v1_pdf_grounding
from app.versions.v1_memory import run_v1_memory


def render_input_bar():

    version = st.session_state.selected_version

    col1, col2, col3 = st.columns([8, 1, 1])

    with col1:

        user_input = st.text_input(
            "Ask something...",
            label_visibility="collapsed"
        )

    pdf_file = None

    with col2:

        if version == "v1.2 PDF Grounding":

            pdf_file = render_pdf_upload()

    with col3:

        send_clicked = st.button("➤")

    if send_clicked and user_input:

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        if version == "v1.0 Basic Chat":

            response = run_v1_basic_chat(user_input)

        elif version == "v1.2 PDF Grounding":

            response = run_v1_pdf_grounding(
                user_input,
                pdf_file
            )

        elif version == "v1.4 Memory":

            response = run_v1_memory(user_input)

        else:

            response = "Version under development"

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        current_chat = st.session_state.current_chat_id

        st.session_state.chat_sessions[current_chat] = (
            st.session_state.messages
        )

        st.rerun()