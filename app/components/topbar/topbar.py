import streamlit as st

from app.common.constants import VERSIONS


def render_topbar():

    col1, col2 = st.columns([8, 2])

    with col1:

        st.markdown("# AITA 🎓")
        st.markdown("AI Teaching Assistant - student edition")

    with col2:

        selected_version = st.selectbox(
            "Architecture",
            VERSIONS,
            key="global_version_selector"
        )

    st.session_state.selected_version = (
        selected_version
    )

    st.markdown("---")