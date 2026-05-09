import streamlit as st
from services.llm_services import generate_response

st.set_page_config(page_title="AITA - Student's Edition", page_icon=":school:", layout="wide")

st.title("AITA - Student's Edition")
st.write("Welcome to the AITA - Student's Edition! This tool is designed to help students get teaching ouside the classroom. Ask any question related to your studies, and I'll do my best to provide a helpful response.")

st.user_input = st.text_area("Ask something...", height=200)

if st.button("Get Response"):
    if st.user_input.strip() == "":
        st.warning("Please enter a question or topic to get a response.")
    else:
        with st.spinner("Thinking..."):
            response = generate_response(st.user_input)
            st.subheader("Response:")
            st.write(response)