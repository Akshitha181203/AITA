from services.llm_services import generate_response


def run_v1_basic_chat(user_input):

    prompt = f"""
    Answer the question using general knowledge.

    Question:
    {user_input}
    """

    return generate_response(prompt)