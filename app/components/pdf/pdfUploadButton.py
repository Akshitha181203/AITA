import streamlit as st


def render_pdf_upload():

    return st.file_uploader(
        "",
        type=["pdf"],
        label_visibility="collapsed"
    )