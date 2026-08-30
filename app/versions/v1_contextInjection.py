from services.llm_services import generate_response
from services.pdf_services import extract_text_from_pdf


def run_v1_pdf_grounding(user_input, pdf_file):

    if pdf_file is None:
        return "Please upload a PDF."

    pdf_text = extract_text_from_pdf(pdf_file)

    prompt = f"""
    Answer ONLY using the PDF.

    PDF Content:
    {pdf_text[:10000]}

    Question:
    {user_input}
    """

    return generate_response(prompt)