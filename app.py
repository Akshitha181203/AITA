import streamlit as st
from services.llm_services import generate_response
import services.pdf_services
from services.quiz_services import generate_quiz

st.set_page_config(page_title="AITA - Student's Edition", page_icon=":school:", layout="wide")

st.title("AITA - Student's Edition")
st.write("Welcome to the AITA - Student's Edition! This tool is designed to help students get teaching ouside the classroom. Ask any question related to your studies, and I'll do my best to provide a helpful response.")

uploaded_file = st.file_uploader("Upload a PDF to extract text", type=["pdf"], key="pdf_uploader")

pdf_text = ""

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = services.pdf_services.extract_text_from_pdf(uploaded_file)
        
    st.success("PDF uploaded successfully!")

if pdf_text:
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = services.pdf_services.generate_summary(pdf_text)
        st.subheader("Summary:")
        st.write(summary)

    if st.button("Generate Quiz"):
        with st.spinner("Generating quiz..."):
            quiz = generate_quiz(pdf_text)
        st.subheader("Quiz:")
        st.write(quiz)

st.user_input = st.text_area("Ask something about the PDF...", height=200)

if st.button("Get Response"):
    if st.user_input.strip() == "":
        st.warning("Please ask a question before getting a response.")
    else:
        with st.spinner("Thinking..."):
            if pdf_text:
                request_prompt = f"""
                        Answer the question ONLY using the provided PDF content.

                        PDF Content:
                        {pdf_text[:10000]}

                        Question:
                        {st.user_input}

                        If the answer is not in the PDF, say:
                        "The PDF does not contain this information."
                    """     # Grounding and Context Injection

                response = generate_response(request_prompt)
                st.subheader("Response:")
                st.write(response)
            else:
                response = generate_response(st.user_input)
                st.warning("Response is from external source")
                st.subheader("Response:")
                st.write(response)