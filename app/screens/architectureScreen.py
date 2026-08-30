import streamlit as st

from app.components.panels.pipelinePanel import (
    render_pipeline_panel
)


def render_architecture_screen():

    st.title("Architecture Overview")

    render_pipeline_panel()