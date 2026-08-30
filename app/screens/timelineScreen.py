import streamlit as st


def render_timeline_screen():

    st.title("Project Evolution")

    timeline = [
        ("✅", "v1.0", "Basic Prompting"),
        ("✅", "v1.2", "PDF Grounding"),
        ("✅", "v1.4", "Memory"),
        ("⬜", "v2.0", "RAG"),
        ("⬜", "v2.1", "Hybrid Retrieval"),
        ("⬜", "v2.2", "Evaluation"),
        ("⬜", "v3.0", "Multi-Agent System")
    ]

    for status, version, description in timeline:

        st.markdown(
            f"{status} **{version}** — {description}"
        )