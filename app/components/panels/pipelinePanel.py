import streamlit as st


def render_pipeline_panel():

    version = st.session_state.selected_version

    if version == "v1.0 Basic Chat":

        st.code("""
User Input
    ↓
Prompt
    ↓
LLM
    ↓
Response
        """)

    elif version == "v1.2 PDF Grounding":

        st.code("""
User Input
    ↓
PDF Injection
    ↓
Prompt Builder
    ↓
LLM
    ↓
Response
        """)

    elif version == "v1.4 Memory":

        st.code("""
User Input
    ↓
Conversation History
    ↓
Prompt Builder
    ↓
LLM
    ↓
Response
        """)

    elif version == "v2.0 RAG":

        st.code("""
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Store
 ↓
Retriever
 ↓
LLM
 ↓
Response
        """)