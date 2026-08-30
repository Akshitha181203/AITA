import streamlit as st

from app.components.panels.metadataPanel import (
    render_metadata_panel
)


def render_limitations_screen():

    st.title("Known Limitations")

    render_metadata_panel("limitations")