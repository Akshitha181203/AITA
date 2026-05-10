import fitz

from services.llm_services import generate_response

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in pdf_document:
        text += page.get_text()
    return text

def generate_summary(pdf_text):
    summary_prompt = f"""
    You are a helpful assistant that summarizes PDF content.

    Based ONLY on the provided PDF content,
    generate a concise summary.

    Rules:
    - Keep the summary clear and concise
    - Do not use outside knowledge

    PDF Content:
    {pdf_text[:8000]}
    """

    response = generate_response(summary_prompt)
    return response