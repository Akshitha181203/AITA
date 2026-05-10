import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text