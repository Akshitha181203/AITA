from services.llm_services import generate_response

def generate_quiz(pdf_text):

    quiz_prompt = f"""
    You are a quiz generator.

    Based ONLY on the provided PDF content,
    generate 5 multiple choice questions.

    Rules:
    - Each question must have 4 options
    - Mention the correct answer
    - Keep questions clear and concise
    - Do not use outside knowledge

    PDF Content:
    {pdf_text[:8000]}
    """

    response = generate_response(quiz_prompt)
    return response