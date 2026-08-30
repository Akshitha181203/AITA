import streamlit as st

from services.llm_services import generate_response


def run_v1_memory(user_input):

    history = st.session_state.messages[-6:]

    context = "\n".join(
        [
            f"{m['role']}: {m['content']}"
            for m in history
        ]
    )

    prompt = f"""
    Use conversation history.

    Context:
    {context}

    User:
    {user_input}
    """

    return generate_response(prompt)