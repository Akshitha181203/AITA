import streamlit as st
import json


def load_current_metadata():

    version = st.session_state.selected_version

    mapping = {
        "v1.0 Basic Chat": "app/metadata/v1_0.json",
        "v1.2 PDF Grounding": "app/metadata/v1_2.json",
        "v1.3 Memory": "app/metadata/v1_3.json",
        "v2.0 RAG": "app/metadata/v2_0.json"
    }

    with open(mapping[version], "r") as file:

        return json.load(file)


def render_metadata_panel(section):

    data = load_current_metadata()

    items = data.get(section, [])

    for item in items:

        st.info(item)