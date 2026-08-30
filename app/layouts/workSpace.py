import streamlit as st

from app.components.sidebar.sidebar import (
    render_sidebar
)

from app.components.topbar.topbar import (
    render_topbar
)

from app.screens.chatScreen import (
    render_chat_screen
)

from app.screens.engineeringNotesScreen import (
    render_engineering_notes_screen
)

from app.screens.architectureScreen import (
    render_architecture_screen
)

from app.screens.limitationScreen import (
    render_limitations_screen
)

from app.screens.timelineScreen import (
    render_timeline_screen
)


def render_workspace():

    render_sidebar()

    render_topbar()

    current_screen = st.session_state.get(
        "current_screen",
        "chat"
    )

    if current_screen == "chat":

        render_chat_screen()

    elif current_screen == "engineering":

        render_engineering_notes_screen()

    elif current_screen == "architecture":

        render_architecture_screen()

    elif current_screen == "limitations":

        render_limitations_screen()

    elif current_screen == "timeline":

        render_timeline_screen()