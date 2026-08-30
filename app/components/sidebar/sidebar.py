import streamlit as st

from app.components.sidebar.navigationMenu import render_navigation_menu
from app.components.sidebar.chatRooms import render_chat_rooms
from app.components.sidebar.newChatButton import render_new_chat_button


def render_sidebar():

    with st.sidebar:

        st.title("AITA")

        render_new_chat_button()

        st.markdown("---")

        render_navigation_menu()

        st.markdown("---")

        render_chat_rooms()