import streamlit as st


def render_navigation_menu():

    if st.button("Engineering Notes"):
        st.session_state.current_screen = "engineering"

    if st.button("Architecture"):
        st.session_state.current_screen = "architecture"

    if st.button("Known Limitations"):
        st.session_state.current_screen = "limitations"

    if st.button("Progress Timeline"):
        st.session_state.current_screen = "timeline"