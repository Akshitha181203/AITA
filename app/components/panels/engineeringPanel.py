import streamlit as st

def EngineeringPanel(selected_version):

    with st.expander("Engineering Notes"):

        st.write(f"""
        Current Version:
        {selected_version}

        Purpose:
        Demonstrate architecture evolution.
        """)

    with st.expander("Internal Pipeline"):

        show_pipeline = st.checkbox(
            "Show Internal Processing"
        )

        if show_pipeline:

            st.code("""
            Prompt Construction
               ↓
            Context Injection
               ↓
            LLM Response
            """)