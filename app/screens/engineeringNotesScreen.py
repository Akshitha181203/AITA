import streamlit as st

from app.components.panels.metadataPanel import (
    render_metadata_panel
)


def render_engineering_notes_screen():

    st.title("Engineering Notes")

    render_metadata_panel("engineering_notes")