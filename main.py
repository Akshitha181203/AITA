import streamlit as st

from app.layouts.workSpace import render_workspace
from app.common.stateManager import initialize_session_state

st.set_page_config(
    page_title="AITA",
    page_icon="🎓",
    layout="wide"
)

initialize_session_state()

render_workspace()