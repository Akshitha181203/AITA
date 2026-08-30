import streamlit as st

from services.pdf_services import generate_summary


def render_summary_panel():

    pdf_text = st.session_state.uploaded_pdf_text

    if not pdf_text:
        return

    st.markdown("---")

    st.subheader("Summary")

    if st.button("Generate Summary"):

        with st.spinner("Generating summary..."):

            summary = generate_summary(pdf_text)

        st.write(summary)