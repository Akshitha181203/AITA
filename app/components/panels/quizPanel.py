import streamlit as st

from services.quiz_services import generate_quiz


def render_quiz_panel():

    pdf_text = st.session_state.uploaded_pdf_text

    if not pdf_text:
        return

    st.markdown("---")

    st.subheader("Quiz")

    if st.button("Generate Quiz"):

        with st.spinner("Generating quiz..."):

            quiz = generate_quiz(pdf_text)

        st.write(quiz)