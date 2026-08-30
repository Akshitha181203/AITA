import streamlit as st

from app.components.chat.chatContainer import (
    render_chat_container
)

from app.components.chat.inputBar import (
    render_input_bar
)

from app.components.panels.summaryPanel import (
    render_summary_panel
)

from app.components.panels.quizPanel import (
    render_quiz_panel
)


def render_chat_screen():

    st.markdown("## AI Workspace")

    render_chat_container()

    render_input_bar()

    if st.session_state.selected_version == (
        "v1.2 PDF Grounding"
    ):

        col1, col2 = st.columns(2)

        with col1:
            render_summary_panel()

        with col2:
            render_quiz_panel()